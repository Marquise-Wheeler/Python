# python file to calculate the average glucose for the day

#================New Program starts here================
from datetime import date

today = date.today()

userInput = input("Please enter your results separated by commas: \n") 
userList = userInput.split(",")
try:
        data_list = [float(number) for number in userList]
except ValueError:
        print("Please enter a comma-delimited list of numbers.")


def list_modifier(data_list):
#Open the text.txt file in write mode.

    """Print the original list, average said list, modify it as needed, and then print again."""
print("Your list is: " + userInput)
average = sum(data_list) / len(data_list) 
# Divide list by sum of elements for x in list var:
x = 1
print("Your modified list is: " + str(data_list))
print("Your average is %.2f" % average)
<<<<<<< HEAD
print("Your average for " + str(today) + " is " + str(average))
file1 = open('glucose_results.py', 'a')
file1.write("Your average is : ")
file1.write('\n')
file1.write(str(average))

=======

# Function call
>>>>>>> feca142e28bb24f827e5631cb35f2b062d52da6d
list_modifier(data_list)


