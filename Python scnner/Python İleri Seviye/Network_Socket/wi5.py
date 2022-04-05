import socket

net = input("Enter network IP address /24")
stl = input("Enter starting value: ")
en1 = input("Enter value final: ")
contain = en1 - st1

net1 = net.split(".")
a = "."

net2 = net1[0] + a + net1[1] + a + net[2] + a
#109.232.219.156
en1 = en1 + 1

def scan(addr):
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = socket.connect_ex((addr,22))
    print(result)
    if result == 0:
        return 1 
    else: 
        return 0
    
 def controll():
     for ip in range(contain):
         addr = net2  + str(ip)
         if(scan(addr)==1):
              print(addr, " e active")
controll()