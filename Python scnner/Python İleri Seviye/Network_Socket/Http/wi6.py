from html.parser import HTMLParser
import urllib.request

answer = urllib.request.urlopen("https://www.gencayyildiz.com/blog/")

satring = answer.read()
satring = str(satring)
# print(satring.decode())

class MiaClasseParser (HTMLParser):
    def handle_start(self, tag, attrs):
        if tag == "a":
            for name, value, value in attrs:
                if name == "href":
                    print(value)
                    
mioParser = MiaClasseParser()
mioParser.feed(satring)