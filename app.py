#how do we access the files on my computer
# load the operating system
import os
# access the directories
os.listdir()
# set the source Directory to the Downloads folder
source_dir = "C:/Users/Mwheeler/Downloads/"
# Scan each directory item as an entry and print the entries
with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)