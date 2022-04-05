import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "10.0.2.15"
port = 8081

serversocket.bind((host,port))

serversocket.listen(5)

while True:
   clientsocket,addr = serversocket.accept()
   mr  = clientsocket.recv(1024)
   print(mr.decode())
   print(addr)
   clientsocket.send(b"Server: Send 404 found error truva!")
   clientsocket.close()
