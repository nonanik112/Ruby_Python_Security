import nmap

primo_port_scanner = nmap.PortScanner()

parm_scans = primo_port_scanner.scan("109.232.219.156", "22", "-sS")

# print(parm_scans)

# print(primo_port_scanner.command_line())

# print(primo_port_scanner.scaninfo())

# print(primo_port_scanner.scanstats())

# print(primo_port_scanner.all_hosts())

# satring = primo_port_scanner["109.232.219.156"].state

# if satring == "up":
#     print("HOST ACTIVE")
# else:
#     print("HOST DOWN")

# print(primo_port_scanner["109.232.219.156"]["tcp"].keys())

#print(primo_port_scanner["109.232.219.156"]["tcp"][22])

print(primo_port_scanner["109.232.219.156"]["tcp"][22]["state"])
