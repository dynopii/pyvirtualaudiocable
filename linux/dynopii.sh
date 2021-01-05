#!/bin/bash
printf '#%.0s' {1..80}
echo " Welcome to dynopii virtual audio cable "
printf '#%.0s' {1..80}
echo ""
echo "Do not kill this terminal"
echo ""
echo "In your conferencing software, choose 'dynopii'/'Monitor of dynopii' etc as your input device, if not already selected"
echo ""

if pactl list short modules | grep -q "sink_name=dynopii" #incase module exists already; i.e. it is not the user's first time
then 
    echo ""
    echo ""
else 
echo "In the pavucontrol window that opens, select 'dynopii' as the playback device where it says: ALSA plug-in[aplay]: ALSA Playback on"
    #this is the part which runs when it is running for the first time
    echo ""
    echo ""
    pacmd load-module module-null-sink sink_name=dynopii_sink sink_properties=device.description=dynopii &
    pavucontrol
fi

#arecord -f cd - | python wire.py | aplay -  Will use this when I can get piping working.
#python hope.py | aplay -f cd       This one should work but I don't know how to work with the subprocess module
#arecord -f cd - | aplay - 
