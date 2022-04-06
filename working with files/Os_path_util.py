# working with Operating System(os) utilities

import os
from os import path
import datetime
from datetime import date,time, timedelta
import time

def main():
    # get os name
    print(os.name)

    # checking existence and file type
    print("File exist:", str(path.exists("fileName.txt")))
    print("Is it file: ", str(path.isfile("fileName.txt")))
    print("Is it directory: ", str(path.isdir("fileName.txt")))

    # actual file path
    print("File path", path.realpath("fileName.txt"))
    print("File path and name", path.split(path.realpath("fileName.txt")))

    # get modification time of file

    t =time.ctime(path.getmtime("fileName.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("fileName.txt")))

    # calculate how long since last modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("fileName.txt"))
    print("it has been",td, "since last modification")
    print("or", td.total_seconds(), "seconds")

    
if __name__ == "__main__":
    main()