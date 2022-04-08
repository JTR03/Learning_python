# collecting internet data

import urllib.request

def main():
    weburl = urllib.request.urlopen("http://www.google.com")
    print("Http code:", weburl.getcode())
    data = weburl.read()
    print(data)

if __name__ == '__main__':
    main()