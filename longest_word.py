#!/usr/bin/python3`

'''
This is a recreation of the python short from @PowerfulPython
The code will take a string and calculate the longest word length.
If there is no even numbered word the code will return "00". Else it
will print the word and store it in the variable longest
'''

# Define the Function, variables and method for calculatin if word has even number of letters

def longest_even_word(text):
    longest = '00' # no text expansion ''
    for word in text.split():
        if len(word) % 2 == 0 and len(word) >= len(longest):
            longest = word
    return longest


# Initialize the strings in a list
strings = [
    "my apple",
    "",
    "Lorem ipsum consectetur adipiscing elit.",
    "a bbb ccccc",
    "The code will take a string and calculate the longest word length.",
    ]

# Loop thru the strings
for string in strings:
    print(f"'{string}' -> '{longest_even_word(string)}'")

