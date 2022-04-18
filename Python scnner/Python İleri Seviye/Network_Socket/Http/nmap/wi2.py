import nmap

parm_port_scanner = nmap.PortScanner()

parm_scans = parm_port_scanner("109.232.219.156", "22", "sS" )

print(parm_scans)