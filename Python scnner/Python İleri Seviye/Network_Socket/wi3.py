import subprocess

net = input("Enter the network address /24:")
netStart = input("Enter the starting value")
netEnd = input("Enter the final value:")

net1 = net.split(".")

#109.232.219.156

# print(net1[0])
# print(net1[1])
# print(net1[2])
# print(net1[3])

netStart2 = int(netStart)
netEnd2 = int(netEnd)

counter = netEnd2 - netStart2

for count in range(counter):
    addressStart = net1[0] + a + net1[1] + a + net1[2] + a + netStart
    status,result = subprocess.getstatusoutput("ping -c 2 " +  addressStart)
    netStart = int(netStart)
    netStart = netStart + 1
    netStart = str(netStart)
    netStart = int(netStart2)
    print(result)