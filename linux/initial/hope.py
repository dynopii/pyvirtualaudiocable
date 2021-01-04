import subprocess
import audioop

cmd = ['arecord', '-f', 'cd', '-']
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
for i in range(16):
    audio = process.stdout.read(160 * 2)
    print(audioop.rms(audio, 2))
process.stdout.close()
process.terminate()