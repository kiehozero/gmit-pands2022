import pandas as pd

# DataFrame creates a table with any number of rows and columns

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# loc prints the returns each key and value from a specified row or rows. The
# second of these will produce an additional dataframe to house the rows.
print(myvar.loc[1])
print(myvar.loc[[0,1]])

# Series a one-dimensional array, but you can assign it labels using the index parameter

a = [1, 7, 2]

b = ["thou", "hund", "tens"]

newVar = pd.Series(a, index=b)

print("tens".format(newVar["tens"]))

# you can use loc again to search for an index
print(newVar.loc["hund"])

# By using a dictionary, you can use key/values as indices

calories = {"day1": 420, "day2": 380, "day3": 390}

dictVar = pd.Series(calories)

print("Calories: {}".format(calories["day2"]))



