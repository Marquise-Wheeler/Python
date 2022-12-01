#!/usr/bin/python3

'''The code has been altered to allow for three seperate conditions.We are checking if the rider is under 12, between 12 and 18, and over 18. '''

print('Welcome to the rollercoaser!')
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaser!")
    age = int(input("What is your age? "))
    if age < 12:
        print("The ticket Price is $5.")
    elif age < 18:
        print("The ticket Price is $7.")
    else:
        print("The ticket Price is $12.")
else:
    print("Sorry, you have to grow taller befor you can ride.")
   
