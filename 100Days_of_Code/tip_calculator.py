# This purpose of this rogram is to cacuate tips.


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welocme to the tip calculator.")

friends = input("How many people will split the bill?\n")
tip = input("What percentage tip would you like to give? 10, 15, or 20%?\n" )
tip_integer = int(tip) / 100
#print(tip_integer)
bill = input("How much is the bill?\n" )
total_bill = float(bill) * float(1 + tip_integer)
friends_integer= int(friends)
cost_person = total_bill / friends_integer
format_cost_person = "{:.2f}".format(cost_person)

print(f"The total cost per person is ${format_cost_person}")
# End of file
