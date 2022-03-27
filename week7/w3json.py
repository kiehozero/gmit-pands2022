import pandas as pd

df = pd.read_json('data.js')

print(df.to_string())

# head will print off the headers and a specified number of rows
print(df.head(10))

# tail will print off the specified number of rows from the bottom up

print(df.tail(10))

# info provides metadata and a summary of information
print(df.info())