import scapy.all as scapy

# 1) arp_request
# 2) broadcast
# 3) response

# --Help komutu
arp_request_packet = scapy.ARP(pdst="10.0.2.1/24")
scapy.ls(scapy.ARP())