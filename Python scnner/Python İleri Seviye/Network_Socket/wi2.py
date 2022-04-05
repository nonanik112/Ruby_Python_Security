import subprocess

ip = "109.232.219.156"

statik, risk = subprocess.getstatusoutput("ping -c 2 " + ip)

if statik == 0:
   print("Il sistem:" + ip + "e attack")
else:
    print("Il sistem:" + ip + "e attack")