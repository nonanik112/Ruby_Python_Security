while True:
   clientsocket,addr = serversocket.accept()
   mr  = clientsocket.recv(1024)
   print(mr.decode())
   print(addr)
   clientsocket.send(b"Server: Send 404 found error truva!")
   clientsocket.close()
