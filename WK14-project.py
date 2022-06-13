# Create a list of services using Python. IE: S3, Lambda, EC2, etc
# 1. The list should be empty initially.
aws_list = []

# 2. Populate the list using append or insert.
aws_list.insert(0, 'S3')
aws_list.append('Lambda')
aws_list.append('EC2')
aws_list.append('DynamoDB')
aws_list.append('RDS')

# 3. Print the list and the length of the list.
print("The list of AWS services is ", aws_list)
length_list = len(aws_list)
print("The # of AWS services is ", length_list)

# 4. Remove two specific services from the list by name or by index.
aws_list.remove("S3")
# 5. Print the new list and the new length of the list.
print("The updated list of AWS services is ", aws_list)
length_list = len(aws_list)
print("The updated # of AWS services is ", length_list)