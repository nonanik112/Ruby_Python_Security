import socket

serverRemote = input("Insert Include IP server remote")
rangePort = input("Enter the port to start scanning")
rangePortFinal = input("Enter the end-of-scan port")

rangePortInitial = int(rangePort)
rangePortFinal = int(rangePortFinal)

for port in range(rangePortFinal, rangePort):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanvio = sock.connect_ex((serverRemote, port))
    if scanvio == 0:
       print("Port {} OPEN".format(port))
    else:
     print("Port {} OPEN".format(port))
    
    sock.close()