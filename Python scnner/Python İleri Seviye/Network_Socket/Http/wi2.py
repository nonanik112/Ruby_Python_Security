import urllib.request

try: 
    reply = urllib.request.urlopen("www.gencayyildiz.com")
    print(reply.read())
    reply.close()
except urllib.request.URLError as errorr:
    print(errorr.reason)