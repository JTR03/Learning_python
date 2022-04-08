# collecting json data from internet

import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count = theJSON["metadata"]["count"]
    print(count, "events recorded")

    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("...............\n")

    for i in theJSON["features"]:
        if (i["properties"]["mag"] > 4.0):
            print(i["properties"]["place"])
    print("...........\n")
    
    print("\n Number of times felt:")
    for i in theJSON["features"]:
        if i["properties"]["felt"] != None:
            if i["properties"]["felt"] > 0:
                print(i["properties"]["place"],i["properties"]["felt"])


def main():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    weburl = urllib.request.urlopen(url)
    print("http code:", weburl.getcode())

    if (weburl.getcode() == 200):
        data = weburl.read()
        printResults(data)
    else:
        print("Could not get data from server")



if __name__ == '__main__':
    main()