# python file to calculate the average glucose for the day

from datetime import date

today = date.today()
#print("Today's date:", today)

#Take input from user and assign it to variables
print("What is your glucose level?")
input1 = input(str())

#Open the text.txt file in write mode.
file1 = open('glucose_results.py', 'a')

#Write the string "Hello, New Stack!" to the file
file1.write(str(today))
file1.write('\n')
file1.write(input1)
file1.write("\n")

#Close the file
file1.close()

 
#Open the text.txt file for appending.
 
 
#Write the content of the variables to the text.txt file
#file1.write(input1)
#file1.write(" ")
#file1.write(input2)
#file1.write("\n")
