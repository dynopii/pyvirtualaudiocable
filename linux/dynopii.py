import subprocess
import audioop

try:    

    print('#' * 80)
    print('Initiating dynopii virtual audio cable ... ')
    loadcmd = ['pacmd', 'load-module', 'module-null-sink', 'sink_name=dynopii_sink', 'sink_properties=device.description=dynopii']
    subprocess.Popen(loadcmd)
    subprocess.Popen('pavucontrol')
    
    cmd0 = ['arecord', '-f', 'cd', '-']
    p0 = subprocess.Popen(cmd0, stdout=subprocess.PIPE) 

    '''
    This stdout of p0 is basically the data we get from arecord, and the data that we can manipulate on the fly and then
    feed to the stdin of the next process p1. 
    If you will work on this, you'll have to replace the stdin=p0.stdout of the following process p1 with your manipulated data.
    '''

    cmd1 = ['aplay', '-f', 'cd', '-']
    p1 = subprocess.Popen(cmd1, stdin=p0.stdout)
    print('')
    print('To quit this program and close your virtual device, press Ctrl-C')
    print('')
    print('#' * 80)
    input()

except EOFError:
    print('EOF Error')

except KeyboardInterrupt:
    print()
    print('Closing the virtual audio cable ....')
    print('Unloading null-sinks ...')
    print('Stopping playback ...')

    uncmd0 = ['pactl', 'list', 'short', 'modules']
    uncmd1 = ['grep', 'sink_name=dynopii']
    uncmd2 = [ 'cut', '-f1' ]
    uncmd3 = [ 'xargs', '-L1', 'pactl', 'unload-module' ]

    unp0 = subprocess.Popen(uncmd0, stdout=subprocess.PIPE)
    unp1 = subprocess.Popen(uncmd1, stdin=unp0.stdout, stdout=subprocess.PIPE)
    unp2 = subprocess.Popen(uncmd2, stdin=unp1.stdout, stdout=subprocess.PIPE)
    unp3 = subprocess.Popen(uncmd3, stdin=unp2.stdout)

    killcmd = ['pkill', 'arecord']  #kill arecord (hence killing ALSA playback since aplay simultaneously stops receiving input via the pipe)
    closefin = subprocess.Popen(killcmd)