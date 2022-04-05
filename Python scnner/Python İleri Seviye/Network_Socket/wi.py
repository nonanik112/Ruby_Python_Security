import subprocess

ip = "109.232.219.156"

statüs, risk = subprocess.getstatusoutput("ping -c 2 " + ip)

print(risk)