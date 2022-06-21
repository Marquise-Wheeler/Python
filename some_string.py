#!/usr/bin/env Python3.7

some_string = "Hello Python\n"
print(some_string)

some_string1 = "The quick brown fox jumped over the lazy dog"
print(some_string1)
some_string2 ='The quick brown fox jumped over the lazy dog\n'
print(some_string2)

first_name = "Monty"
last_name = "Python"
print(first_name+last_name)
# print with space separating first and last name
print(first_name+ " " + last_name)

# Using variables in strings
print("\nMy first name is {}. My family name is {}\n".format(first_name, last_name))

print("Using f strings to include variables in your strings")
firstname = "Marquise"
lastname = "Wheeler"
print(f"My first name is {firstname}. My family name is {lastname}")
