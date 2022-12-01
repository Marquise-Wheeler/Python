#!/usr/bin/env python3
print("Welcome to the tip calculator.")

# User input
bill = input("How much is the bill?\n" )
tip = input("What percentage tip would you like to give? 10, 15, or 20%?\n" )
friends = input("How many people will split the bill?\n")

# Calculations
tip_integer = int(tip) / 100
total_bill = float(bill) * float(1 + tip_integer)
friends_integer= int(friends)
cost_person = total_bill / friends_integer
format_cost_person = "{:.2f}".format(cost_person)

# Print statement
print(f"The total cost per person is ${format_cost_person}")

# End of file
