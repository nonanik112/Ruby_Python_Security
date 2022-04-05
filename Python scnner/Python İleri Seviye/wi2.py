import socket

stringa = socket.gethostbyname("gencayyildiz.com")
print(stringa)

stringa2 = socket.gethostbyname_ex("gencayyildiz.com")
print(stringa2)

stringa3 = socket.getfqdn("gencayyildiz.com")
print(stringa3)

stringa4 = socket.gethostbyaddr("8.8.8.8")
print(stringa4)

stringa5 = socket.getservbyname("https")
print(stringa5)

stringa6 = socket.getservbyport(443)
print(stringa6)

