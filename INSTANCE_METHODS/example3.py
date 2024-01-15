# Example 3: Interaction between Methods

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Creating an instance of Rectangle
rectangle = Rectangle(length=5, width=3)

# Calling methods that use self to interact with instance variables
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print(f"Area: {area}")              # Output: Area: 15
print(f"Perimeter: {perimeter}")    # Output: Perimeter: 16

