import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "109.232.219.156"
port = 8080

message = bytearray("-" * 50, "UTF-8")

s.connect((host,port))

s.send(b"message by client 3: client server")

print(s.recv_into(message))
print(message)
