import pandas as pd

# DataFrame creates a table with any number of rows and columns

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# Series a one-dimensional array, but you can assign it labels using the index parameter

a = [1, 7, 2]

b = ["thou", "hund", "tens"]

newVar = pd.Series(a, index=b)

print("tens".format(newVar["tens"]))

# By using a dictionary, you can use key/values as indices

calories = {"day1": 420, "day2": 380, "day3": 390}

dictVar = pd.Series(calories)

print("Calories: {}".format(calories["day2"]))



