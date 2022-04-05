from urllib.request import Request
from urllib.request import urlopen

resquest = Request("https://www.gencayyildiz.com/blog/")

urlopen(resquest)

print(resquest.get_header("User-agent"))