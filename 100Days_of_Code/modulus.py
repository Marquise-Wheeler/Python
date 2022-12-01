#!/usr/bin/python3

# Day 3 Challenge: Create a program that can determine if a number is odd or even 12/1/2022.


number = int(input("What number do you eant to check? "))
if number % 2 == 0:     # the problem I encountered here was I forgot the colon and that caused a syntax error
   print("This is a even number.")
else:
    print("This is an odd number.")
