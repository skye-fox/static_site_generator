"""Primary module of the program"""

import os
import shutil

from copystatic import copy_static_dir


def main():
    """Entry point function for the program"""
    if os.path.exists("public/"):
        print("***** Removing public directory *****")
        shutil.rmtree("public/")
    print("***** Creating public directory *****")
    os.mkdir("public/")
    copy_static_dir("static/", "public")


main()
