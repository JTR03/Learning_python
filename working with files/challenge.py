# answer to end of chapter challenge
# get all files of current directory
# insert them int a new directory
# calculate total byte size

import os
from os import path

def main():
    files = os.listdir()
    bytes = 0

    for x in files:
        if (path.isfile(x)):
            size = path.getsize(x)
            bytes += size
    
    os.mkdir("result")

    myFile = open("result/txtfile.txt","w+")
    
    if(myFile.mode == "w+"):
        myFile.write("Total: "+ str(bytes) + " bytes \n")
        myFile.write("list of files: \n")
        for i in files:
            if (path.isfile(i)):
                myFile.write(i + '\n')
        myFile.close()


        

if __name__ == "__main__":
    main()
