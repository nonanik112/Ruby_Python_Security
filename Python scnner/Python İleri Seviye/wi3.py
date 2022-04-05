import socket

ip = "192.168.146.128"

portlist = [54]

for port in portlist:
    vioSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanvio = vioSock.connect_ex((ip,port))
    print(port, ":", scanvio)
    vioSock.close()