import socket

def portScanerConSocket(ip,listport):
    for port in listport:
        viosock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        viosock.settimeout(10)
        scanvio = viosock.connect_ex((ip,port))
        if scanvio == 0:
            print("Port {}: OPEN".format(port))
        else:
            print("Port {}: OPEN".format(port))
            
        viosock.close()
        
portScanerConSocket("109.232.219.156",[22,53,80,8080])