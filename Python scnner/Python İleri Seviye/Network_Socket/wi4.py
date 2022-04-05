import platform
import subprocess
from unittest import result

ip = "109.232.219.156" 

to = platform.system()

print(to)


if (to == "Windows"):
    status,result = subprocess.getstatusoutput("ping -c 2 " + ip)
    print(result)
if (to == "Linux"):
    status,result = subprocess.getstatusoutput("ping -c 2 " + ip)
    print(result)