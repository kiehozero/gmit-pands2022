# The original task was "Write a program that takes in a float and outputs an int rounded down.
# Enter a float number: 5.99
# 5.99 floored is 5."

import math

userInput = float(input("Enter a float number: "))
floorValue = math.floor(int(userInput))

print("{} floored is {}".format(userInput, floorValue))