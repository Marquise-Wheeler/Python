# python file to calculate the average glucose for the day

#================New Program starts here================
userInput = input("Please enter your results separated by commas: \n") 
userList = userInput.split(",")
try:
        data_list = [float(number) for number in userList]
except ValueError:
        print("Please enter a comma-delimited list of numbers.")


def list_modifier(data_list):
    """Print the original list, average said list, modify it as needed, and then print again."""
print("Your list is: " + userInput)
average = sum(data_list) / len(data_list) 
# Divide list by sum of elements for x in list var:
x = 1
print("Your modified list is: " + str(data_list))
print("Your average is %.2f" % average)

# Function call
list_modifier(data_list)
