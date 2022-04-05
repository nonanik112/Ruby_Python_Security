import socket

host = "10.0.2.15"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:

     s.bind((host,port))
     s.settimeout(5)
     data, addr = s.recvfrom(1024)
     print(addr)
     print("Message Port UDP e: ", data.decode() )
     s.close()
except socket.timeout:
     print("Server IP Data Error 400 found")
     s.close()