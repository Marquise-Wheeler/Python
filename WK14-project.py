# This project I will be using Cloud9's python environment to create a list and add items to it.
# Creating an empty list to hold the items.
aws_list = []

# Populating the list using two different methods, insert and append.
aws_list.insert(0, 'S3')
aws_list.append('Lambda')
aws_list.append('EC2')
aws_list.append('DynamoDB')
aws_list.append('RDS')

# Displaying the created list using the print function.
print("The list of AWS services is ", aws_list)

# Storing the length of the list to a new variable using the len function and display to screen with print.
length_list = len(aws_list)
print("The # of AWS services is ", length_list)

# Removing items from list using the name of the item.
aws_list.remove("S3")
aws_list.remove("RDS")

# Print the new list and the new length of the list. 
print("The updated list of AWS services is ", aws_list)
length_list = len(aws_list)
print("The updated # of AWS services is ", length_list)