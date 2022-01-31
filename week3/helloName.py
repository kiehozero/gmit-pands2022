# helloName is written in camelCase
# uses a variable to greet author

name = "Eric Cantona"

print("Hello"  + name)

# below won't work because Python wants to add the integer to another

age = 99

print("Your age is " + str(age))
print("Your age is {}".format(age))

print("Your name is {}, and you are {} years old.".format(name,age))