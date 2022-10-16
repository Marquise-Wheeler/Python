# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Verify variable types
# print(type(height))
# print(type(weight))

# Convert variables and perform calculations
bmi = int(weight) / float(height) ** 2

#Declare new variable to hold bmi_integer
bmi_integer = int(bmi)
print("Your current BMI is : " + str(bmi_integer))   # String concatenation
print(f"Your current BMI is : {bmi_integer}")        # f-string
