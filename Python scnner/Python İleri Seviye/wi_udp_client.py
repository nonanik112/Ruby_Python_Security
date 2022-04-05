import socket

host = "10.0.2.15"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(s.sendto(b"message",(host,port)))

s.close()