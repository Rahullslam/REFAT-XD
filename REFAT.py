import os
os.system('git pull')
from os import path,system
from platform import uname
op = uname().machine.lower()
if 'aarch' in op:
    if path.isfile("XD.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/REFAT-156/PRO-XD/main/xd -o xd")
else:exit('\033[1;31m\n[•] Sorry System Or 32bit Device Not Supported ')
os.system('chmod 777 xd && ./xd')
