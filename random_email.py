#!/usr/bin/env Python3

# this will create fake emails to use with my database project

import random
import string

email_list = []
num = 0                                                                 # initialized variable to track iterations.
# = int(input('How many emailss do you need ? '))

def random_char(y):
        return ''.join(random.choice(string.ascii_lowercase) 
        for x in range(y))
        
uniq_email=(random_char(8)+"@gmail.com")
print(uniq_email)
email_list.append(uniq_email)
print(email_list)