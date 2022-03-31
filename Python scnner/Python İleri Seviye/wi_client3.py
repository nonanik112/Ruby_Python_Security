import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "10.0.2.15"
port = 80

message = bytearray("-" * 50, "UTF-8")

s.connect((host,port))

s.send(b"message by client 3: client server")

print(s.recv_into(message))
print(message)
