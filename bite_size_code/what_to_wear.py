#!/usr/bin/env python3

# Ask the user to input the current temperature
temperature = int(input('What is the current temperature? '))

# Compare the temp and provide clothing suggestions
if temperature >= 80:
    outfit = 'shorts and pack your sunglasses'
elif temperature <= 79 and temperature >= 60:
    outfit = 'a light jacket'
else:
    outfit = 'a coat in addition to a hat, gloves, and scarf'

# Advice  for user
advice = (f'Today you should wear {outfit}.')

print (advice)

