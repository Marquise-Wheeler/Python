#!/usr/bin/python3

# Date: 03/26/2023
# DMOJ problem: wc16c1j1
# This program allows the user to rate the spookiness of the festival
# It utilizes string concantenation, print statements and multiplication


# Declare range variables
x = 2
y = 20

def checkRange(num):
    if x <= num <= y :
        print('The number {} is in range({}, {})'.format(num, x,y))
    else:
        print('The number {} is not in range ({}, {})'.format(num, x,y))

factor = []
rating = "o"
# factor = int(input("Enter your spooky factor betweeen 2 and 20: "))
str1 = "sp"
str2 = "ky"
# result = (str1 + (rating * factor) + str2)



# print(result)
