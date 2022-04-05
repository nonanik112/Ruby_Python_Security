import urllib.request
import urllib.error

try:
    url = "https://www.gencayyildiz.com/blog/"
    respost = urllib.request.urlopen(url)
    print("The Status code e: ", str(respost.code))
    if respost.code == 200:
        print(respost.headers)
        
except urllib.error.URLError as errorr:
       print("URL not correct")
       print(errorr.reason)      
             
except urllib.error.HTTPError as errorr2:
       print("URL not correct")
       print(errorr2.reason)