import requests
from requests.auth import HTTPDigestAuth

anwers = requests.get("https://www.gencayyildiz.com/blog/HTTP/Digest", auth= HTTPDigestAuth("guest", "guest"))


print("Codding HTML in anwer" + str(anwers.status_code))

if anwers.status_code == 200:
    print("Authentication" + anwers.text)