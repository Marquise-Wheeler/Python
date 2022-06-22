#1/usr/bin/env Python

# Lists

fruit = ["apples", "oranges", "bananas"]
fruit.append("strawberry")
print(fruit)

# Assigning [] to a variable
fruit1 = []

# using the list constructor
fruit2 = list()


print(len(fruit))
print(fruit[-1])
print(fruit[-2])

# Using insert

fruit.insert(2, "kiwi")
print(fruit)

''' Organizing a list using the sorted function does 
not change the original list '''
print(sorted(fruit))

# Sort method changes the original list
fruit.sort()
print(fruit)

# print list in reverse order to undo issue the command again
fruit.reverse()
print(fruit)

# Delete item from a list
del fruit[1]
print(fruit)

# Using pop to store a deleted variable returns last item by default
favorite_fruit = fruit.pop()
print(favorite_fruit)

# using pop with index to return a specific item
fresh_fruit = fruit.pop(1)
print(fresh_fruit)

print(fruit)

# removing an item by value using remove method
fruit.remove('bananas')
print(fruit)