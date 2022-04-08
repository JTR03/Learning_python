# parsing and processing HTML

import urllib.request
from html.parser import HTMLParser

paragraph = 0

class myHTMLparser(HTMLParser):
    def handle_comment(self,data):
        print("encounter a comment:", data)
        pos = self.getpos()
        print("At line:", pos[0], "position:", pos[1])

    def handle_starttag(self,tag,attrs):
        print("Ecountered start tag",tag)
        pos = self.getpos()
        print("At line:",pos[0],"position",pos[1])

        global paragraph
        if tag == "p":
            paragraph += 1

        if len(attrs) > 0:
            print("Atrributes:")
            for i in attrs:
                print("\t", i[0],"=",i[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("encountered text data", data)
        pos = self.getpos()
        print("At line:",pos[0],"position:",pos[1])

def main():

    parser = myHTMLparser()

    url = "https://www.medhubbsa.co.za"

    weburl = urllib.request.urlopen(url)
    code = weburl.getcode()
    print("code is:", code)

    if (code == 200):
        data = weburl.read()
        parser.feed(str(data))

    else:
        print("Could not fet data", code)

    print("paragraphs tag",paragraph )

if __name__ == "__main__":
    main()