#!/usr/bin/python

import subprocess
try:
    with open("afile", 'w') as f:
        for i in range(24):
            ass = subprocess.run([f'''ping 192.168.1.{i} -c 1 | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" '''], capture_output=True, shell=True, text=True)
            if (ass.stdout != b''):
                print(ass.stdout, file=f)
except KeyboardInterrupt:
    exit()
    
# stdout=subprocess.DEVNULL    

