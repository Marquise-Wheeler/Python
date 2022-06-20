#!/usr/bin/python3

# This progam will allow the user to input the number of unique names needed for the EC2 instances in their Environment.
# After recieving the number the program will generate a unique name that includes the dept, 4 digits and 3 letters.

# Import libraries
import random
import string

# Assign.Initialize  variables
characters = string.ascii_lowercase                                        # used to generate random lowercase strings.
env_names = []                                                          # empty dictionary to store instance names.                     
num = 0                                                                 # initialized variable to track iterations.
instances = int(input('How many instances do you need names for? '))    # Prompt user input of # names.
dept_name = input('What is the name of your department? ')              # Prompt for department name.              
print(instances)                                                        # Output to verify user input

# Begin while loop to create names.
while (num < instances):
    num = num + 1                                                       # Increment count by 1
    unique_num = str(random.randrange(0000, 9999))                      # Change rand.range to string store in variable
    unique_char = ''.join(random.sample(string.ascii_lowercase, 3))     # use .sample so string is not duplicated 
    uniq_name = dept_name + unique_num + unique_char                    # concantenate strings to create unique name
    env_names.append(uniq_name)                                         # Add names to the list.

print(env_names)
