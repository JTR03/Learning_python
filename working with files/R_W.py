# Reading and writing files in python

def main():
    # opening and/or creating a .txt file
    myFile = open("fileName.txt","w+")

    # append new data to existing file

    myFile = open("fileName.txt","a+")

    # writing data into the created file
    for i in range(10):
        myFile.write("Appended Content of file\n")

    # close file when done
    myFile.close()

    # reading file content
    myFile = open("fileName.txt","r")
    if(myFile.mode == "r"):
        content = myFile.read()
        print(content)

        # reading file lines
        fl = myFile.readlines()
        for x in fl:
            print(x)
if __name__ == "__main__":
    main()