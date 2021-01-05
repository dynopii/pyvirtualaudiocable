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
    print('Closing the virtual audio cable ....')
    print('Unloading null-sinks ...')
    print('Stopping playback ...')
    subprocess.Popen('./close.sh')
