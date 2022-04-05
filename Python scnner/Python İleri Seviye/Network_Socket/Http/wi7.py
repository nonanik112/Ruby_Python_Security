import requests 

from requests.auth import HTTPBasicAuth

anwers = requests.get("https://www.gencayyildiz.com/blog/", auth= HTTPBasicAuth("guest", "guest"))

print("Codding HTML in anwer" + str(anwers.status_code))

if anwers.status_code == 200:
    print("Authentication" + anwers.text)