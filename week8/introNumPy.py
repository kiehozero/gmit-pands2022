import numpy as np

list = [1,2,3,4,5,6,7]
numbers = np.array([1,2,3,4,5,6,7])

# below is not a valid operation in traditional python, but in numpy it is
# list = list + 3

print(list)

# note that this performs the +3 calculation on every item in the variable
numbers = numbers + 3
print(numbers)

# you can even multiply an array by another array of the same length
numbers = numbers * np.array([1,4,1,4,1,4,1])

print(numbers)

randomNum = np.random.randint(100,200,10)

print(randomNum)

normDistro = np.random.normal(100,1,10)

print(normDistro)