import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 8080

s.connect((host,port))

i = 0
while i<5:
   stringa = b"Message by Client1: Server!"
   s.send(stringa)
   i = i + 1

tm = s.recv(1024)
print(tm.decode())
s.close()
