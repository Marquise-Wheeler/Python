

#!/usr/bin/env python3.7
"""
Name: cwd_script.py 
Date : 06/20/2022 
This file is for taking notes on the lectures I am watching.
This lecture series is from LinkedIn Learning on working with Files
https://www.linkedin.com/learning/python-working-with-files/use-os-module-to-uncover-path-and-file-details?autoSkip=true&autoplay=true&resume=false&u=2203402
File types cintain data od different types
the built-in OS module provides functionality for interacting
with the operating system.
"""
import os

def display_cwd():              # display_cwd is the name we give the function
    cwd = os.getcwd()           # Assign variable cwd
    print("Current Working Directory: ", cwd)
 
def up_one_direcory_level():    # Create new function
    os.chdir("../")             # hard code syntax to go up one level

def display_entries_in_directory(directory):
    # os.listdir()
    with os.scandir(directory) as entries:
        for entry in entries:
            print (entry.name)
# Function calls       
if __name__ =="__main__":
    display_cwd()
    up_one_direcory_level()
    display_cwd()
    display_entries_in_directory("PYTHON/python-everything/LearnPython3HW")







# ===================================================================