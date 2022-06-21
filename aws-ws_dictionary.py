#!/usr/bin/env Python3


user = {"first_name":"Ada"}         #Create user key-value
print(user)

account_details = {}                #Create empty dictionary.

# account_detail = dict()             # use dict constructor to create dictionary

print(user["first_name"])

# Add a key-value Distionaries are mutable(can be changed)
user["family_name"] = "Byron"
print (user)

# Modify a value
user["family_name"] ="Lovelace"
print(user)

# Delete a Key-Value Pair
del user["family_name"]
print(user)