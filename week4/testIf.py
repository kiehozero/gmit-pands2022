# basic if formatting

userNo = int(input("Enter a number: "))
if userNo % 2 == 0:
    print("{} condition is even".format(userNo))
else:
    print("{} is odd".format(userNo))

# basics of elif

if (userNo % 2) == 0:
    print(userNo, " is even")
elif (userNo % 3) == 0:
    print(userNo, " is divisible by 3")
else:
    print(userNo, "is not even or divisible by 3")

print("Thank you for testing", userNo)