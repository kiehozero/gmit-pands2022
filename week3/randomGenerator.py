import random

# lab answer used randint instead of randrange
randNum = random.randrange(1, 10)

print(randNum)

userStart = int(input("Enter a start number: "))
userEnd = int(input("Enter an end number: "))
userRand = random.randint(userStart, userEnd)
print("Your random number is: {}".format(userRand))