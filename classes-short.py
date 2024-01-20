#!/usr/bin/python3

# Python short on creating classes

# Python Classes
class Person:
    def __init__(self, name):
     self.name = name

    def say_hello(self):
        print("Hello {}!".format(self.name))

marquise = Person('Marquise')
marquise.say_hello()
