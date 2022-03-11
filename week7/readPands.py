# from Real Python tutorial, showing how quickly pandas can make a dataframe

import pandas

# use the index_col parameter to change from Python's default zero-index to the one-index you'd see in Excel
# use the parse_dates parameters to format dates accordingly
# use the names parameter to set the column headers as list variable
df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])

print(df)

# confirms format of date that has been parsed
print(type(df['Hire Date'][0]))