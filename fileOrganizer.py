import sys
import time
import random

import os
import shutil

# Add the path of you "Downloads" folder.
from_dir = "C:/Users/LENOVO/Downloads"
# Create "Document_Files" folder in your Desktop and update the path accordingly.
to_dir = "C:/Users/LENOVO/Downloads/Organized_Files"


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


list_of_files = os.listdir(from_dir)
#print(list_of_files)

# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    for key, value in dir_tree.items():

        if extension in value:

            path1 = from_dir + '/' + file_name  # source
            path2 = to_dir + '/' + key  # folder path
            path3 = to_dir + '/' + key + '/' + file_name  # destination

            if os.path.exists(path2):

                print("Directory Exists...")
                print("Moving " + file_name + "....")
                shutil.move(path1, path3)
                time.sleep(1)

            else:
                print("Making Directory...")
                os.makedirs(path2)
                print("Moving " + file_name + "....")
                shutil.move(path1, path3)
                time.sleep(1)
