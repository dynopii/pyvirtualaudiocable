import subprocess
import audioop

try:    
        chmods0 = ['chmod', '755', 'dynopii.sh']
        chmods1 = ['chmod', '755', 'close.sh']
        subprocess.Popen(chmods0)
        subprocess.Popen(chmods1)
        
        cmd0 = ['./dynopii.sh']
        p0 = subprocess.Popen(cmd0)
        cmd = ['arecord', '-f', 'cd', '-']
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        cmd2 = ['aplay', '-f', 'cd', '-']
        p2 = subprocess.Popen(cmd2, stdin=process.stdout)
        print('#' * 80)
        print()
        print('To quit this program and close your virtual device, press Ctrl-C')
        print()
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

    killcmd = ['pkill', 'arecord']  #kill the arecord (hence killing ALSA playback)
    closefin = subprocess.Popen(killcmd)