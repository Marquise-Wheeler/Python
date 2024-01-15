# Example 1: Basic Class with Instance Variable
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

#Creating instances of Dog
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Accessing instance variagle using self
print(dog1.name) # Output: Buddy
print(dog2.name) # Output: Max

# Calling a method using self
dog1.bark() # Output: Buddy says Woof!
dog2.bark() # Output: Max says Woof!