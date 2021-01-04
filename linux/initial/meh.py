#!/usr/bin/python
#
# Equivalent to:
#
# arecord -f S16_LE -r48000 -c2 -F0 --period-size=1024 -B0 --buffer-size=4096 \
#    -D ${SOURCE_DEVICE} | aplay -D ${DESTINATION_DEVICE}
#
# But instead, this will run as a single executable that is not the same as
# aplay.

import pyalsaaudio as alsaaudio
import argparse
import struct

def pipe(in_card, out_card, channels=2, rate=48000, periodsize=128, floor_noise=0):
  format = alsaaudio.PCM_FORMAT_S16_LE
  in_device = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NORMAL, in_card)
  in_device.setchannels(channels)
  in_device.setrate(rate)
  in_device.setformat(format)
  in_device.seetperiodsize(periodsize)

  out_device = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, alsaaudio.PCM_NORMAL, out_card)
  out_device.setchannels(channels)
  out_device.setrate(rate)
  out_device.setformat(format)
  out_device.setperiodsize(periodsize)

  try:
    while True:
      length, buf = in_device.read()
      buffer_silent = floor_noise and is_silent(length, buf, floor_noise)
      try:
        if length > 0 and not buffer_silent:
          out_device.write(buf)
      except alsaaudio.ALSAAudioError:
        print('Possible failed to provide proper frame size: %d' % length)
  except KeyboardInterrupt:
    pass

def is_silent(length, buf, floor_noise):
  """Returns True if the clip is nearly silent."""
  samples = len(buf) / 2  # each sample is a short (16-bit)
  values = struct.unpack('<%dh' % samples, buf)
  for v in values:
    if abs(v) > floor_noise:
      return False
  return True


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', '-i', help='Input card name')
  parser.add_argument('--output', '-o', help='Output card name')
  parser.add_argument('--verbose', '-v', action='store_true', help='Verbose')
  parser.add_argument('--floor-noise', type=int,  default=0,
                      help='Mute when samples are nearly silent')
  args = parser.parse_args()

  if args.verbose:
    print("Cards: ")
    for card in alsaaudio.cards():
      print('  ', card)
    print('PCMs: ')
    for pcm in alsaaudio.pcms():
      print('  ', pcm)

  pipe(args.input, args.output, floor_noise=args.floor_noise)