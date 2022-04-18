import nmap

parm_port_scanner = nmap.PortScanner()

parm_scans = parm_port_scanner("109.232.219.156", "22,80,53,8080", "-sS")

for host in parm_port_scanner.all_hosts():
    print("Host scan: ", (host))
    print("Its status and: ", parm_port_scanner[host].state())

for protocoll in parm_port_scanner[host].all_protocols():
    print("Its protocol an: ", protocoll)
    port = parm_port_scanner[host][protocoll].keys()

for portt in port:
    print("Port number: ", (portt), "Status ", parm_port_scanner[host][protocoll][portt]["state"])