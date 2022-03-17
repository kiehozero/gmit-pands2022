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

print(type(numbers))

# you can add array elements together
sum = numbers[2] + numbers[3]
print(f"{numbers[2]} plus {numbers[3]} equals {sum}")

randomNum = np.random.randint(100,200,10)

print(randomNum)

normDistro = np.random.normal(100,1,10)

print(normDistro)

conv = np.array([["type",1,2,3],["mph",10,20,30],["kph", 20,30,50]])

print(conv)

# ndim returns the number of dimensions an array has
dimCount = conv.ndim

print(f"Conv has {dimCount} dimensions")

# you can preset the number of dimensions required using ndmin, I guess
# this is to allow for stuffing of blank dimensions at a later stage?
arr = np.array([["a", "b", "c", "d"], [1,2,3,4]], ndmin=4)
dims = arr.ndim

print(arr)
print(f"Arr has {dims} dimensions")

# you can access array elements using comma-separated integers
# note the zeroes below are because of the additional dimensions specified by ndmin
print(f"The third element on the first row of the fourth dimension is {arr[0,0,1,3]}")