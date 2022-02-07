import scapy.all as scapy

arp_response = scapy.ARP(op=2,pdst="10.0.2.15")
scapy.ls(scapy.ARP)
