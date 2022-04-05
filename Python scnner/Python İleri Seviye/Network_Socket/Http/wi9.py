from bs4 import BeautifulSoup
import requests
import html5lib
import json

url = "https://www.gencayyildiz.com/blog/"

anwers = requests.get(url)

data = anwers.text
# print(data)

Beautifulsoup = BeautifulSoup(data, "html5lib")

# for link in Beautifulsoup.find_all("a"):
#     print(link.get("href"))
     
# for form in Beautifulsoup.find_all("form"):
#     print(form)
    
# for metatag in Beautifulsoup.find_all("meta"):
#     print(metatag)
    
for json in Beautifulsoup.find_all("id"):
    print(id.json)