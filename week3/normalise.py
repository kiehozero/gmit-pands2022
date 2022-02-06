# Write a program (normalise.py) that reads in a string and strips any leading
# or trailing spaces, the program should also convert the string to lower case.
# The program should also output the length of the input and output strings. See 
# Python - String Methods (w3schools.com) for more information of string methods.

userInput = input("Please enter a string: ")
lenInput = len(userInput)
normalStr = userInput.lower().strip()
lenNormal = len(normalStr)

print(
    "That string normalised is: {}.\nWe reduced the input string from {} to {} characters."
    .format(normalStr, lenInput, lenNormal)
    )