# How to raise an exception

try:
    varInp = input("Please enter a number: ")
    number = int(varInp)
    if (number < 0):
        raise ValueError("Negative value entered.")
    multi = number * 2
    print(f"{number} multiplied by 2 is {multi}")
except ValueError as e:
    # will print line 12 for all ValueErrors
    print("Please enter a number only.")
    # will print out the addition message at line 7 if criteria is met
    print(e)