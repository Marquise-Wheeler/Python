# Example 2: Class Method with Parameter
class Calculator:
    def __init__(self, result=0):
        self.result = result
    
    def add(self, x):
        self.result += x

    def subtract(self, x):
        self.result -= x
    
    def display_result(self):
        print(f"Result: {self.result}")
    
# Creating an instance of Calculator
calc = Calculator()

# Performing calculations using methods with self
calc.add(25)
calc.subtract(3)
calc.display_result() # Output: Result: 2
    