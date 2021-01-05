#
## Requirements:-
    pavucontrol, python module subprocesss, audioop
#
#### Step 1:
    Run the script with the command:
    `$ python3 dynopii.py`

#### Step 2:
    In the "Playback" tab of the pavucontrol window that opens, and make sure that the playback device for the running "ALSA plug-in[aplay]: ALSA Playback _on_" is 'dynopii'. 

#### Step 3:
    In your conferencing software, select '_Monitor of dynopii_' as your audio input device.

And your microphone audio is now routed to the conference!
#
To close this, stop the script using `Ctrl-C` and it will also delete the virtual device module and stop the playback.