import http.client

connect = http.client.HTTPConnection("www.gencayyildiz.com")

connect.request("GET", "page/post" )

responseServer = connect.getresponse()

#print(responseServer)

print(responseServer.status, responseServer.reason)

dat = responseServer.read()
print(dat.decode())