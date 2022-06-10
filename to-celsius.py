#/usr/bin/python3

# This script prompts the user for information, displays the information and converts it to a differnt temperature scale.
# Date: 06092022

# Python implementation goes here

fahrenheit = float(input("What temp (in Fahrenheit) woould you like converted to Celsius? "))


celsius = (fahrenheit - 32) * 5 / 9


print(fahrenheit, "F is", round(celsius, 2), "C")