import imp
from urllib.request import Request
from urllib.request import urlopen

resquest = Request("https://www.gencayyildiz.com/blog/")
resquest.add_header("Kategoriler", ".Net6")

restpost = urlopen(resquest)
restpost2 = restpost.read()

print(restpost2.decode())