# working fileSystem shell methods

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile
import zipfile


def main():
    # making a duplicate of existing file
    if (path.exists("fileName.txt.bak")):
        # get the actual path of file
        src = path.realpath("fileName.txt")

        # make a backup copy
        # dst = src + ".bak"
        # shutil.copy(src, dst)

        # rename the original file
        # os.rename("fileName.txt","newName.txt")

        # making a zip folder with all files in it
        # root_dir,tail = path.split(src)
        # shutil.make_archive("archive","zip", root_dir)

        # fine-grained control over zip files
        with ZipFile("testzip.zip","w") as newzip:
            newzip.write("newName.txt")
            newzip.write("fileName.txt.bak")

if __name__ == "__main__":
    main()