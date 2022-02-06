# round always rounds to nearest even number, for traditional
# rounding use math.ceil() and math.floor(), or go to 
# https://realpython.com/python-rounding/ for more information.

userinput = float(input("Enter a float number: "))
rounded = round(userinput)

print("{} rounded is {}".format(userinput,rounded))