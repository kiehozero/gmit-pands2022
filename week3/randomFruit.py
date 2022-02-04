import random

fruitList = ["apple", "banana", "cherry", "strawberry", "orange"]

print(random.choice(fruitList))

# lab answer added the following:
# index = random.randint(0, len(fruitList)-1)
# fruit = fruitList[index]
# print("A Random Fruit: {}".format(fruit))