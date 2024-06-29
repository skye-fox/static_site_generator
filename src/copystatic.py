"""Module to copy files from static directory to public directory"""

import os
import shutil


def copy_static_dir(src, dest):
    """Function to recursively copy a src directory to a destination directory"""
    dir_list = os.listdir(src)
    for file in dir_list:
        file_path = os.path.join(src, file)
        if not os.path.isfile(file_path):
            new_dir = os.path.join("public/", file)
            print(f"***** Creating {new_dir} directory *****")
            os.mkdir(new_dir)
            copy_static_dir(file_path, new_dir)
        if os.path.isfile(file_path):
            print(f"***** Copying {file_path} to {dest} directory *****")
            shutil.copy(file_path, dest)
