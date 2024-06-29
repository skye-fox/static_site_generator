"""Primary module of the program"""

import os
import shutil

from copystatic import copy_static_dir
from gencontent import generate_page

DIR_PATH_CONTENT = "./content"
DIR_PATH_PUBLIC = "./public"
DIR_PATH_STATIC = "./static"
TEMPLATE_PATH = "./template.html"


def main():
    """Entry point function for the program"""
    if os.path.exists(DIR_PATH_PUBLIC):
        print("***** Removing public directory *****")
        shutil.rmtree(DIR_PATH_PUBLIC)
    print("***** Creating public directory *****")
    os.mkdir(DIR_PATH_PUBLIC)
    copy_static_dir(DIR_PATH_STATIC, DIR_PATH_PUBLIC)
    generate_page(
        os.path.join(DIR_PATH_CONTENT, "index.md"),
        TEMPLATE_PATH,
        os.path.join(DIR_PATH_PUBLIC, "index.html"),
    )


main()
