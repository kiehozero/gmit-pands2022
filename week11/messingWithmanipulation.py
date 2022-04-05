# demonstrate reading from TSV and excel
# Author Andrew Beatty

import pandas as pd
import re
import numpy as np
import dataManipulation

filename = 'originalData.tsv'

df = pd.read_table(filename)
# you can print individual columns by adding a list after the filename, or in this case assign it to a variable first
listOfCols = ['Module ID', 'Duration']
# the head command will print the first few columns
print(df[listOfCols].head(2))

# loc will return data from a given indexed row, if you haven't specified an index, it defaults to the row number
dfr = pd.DataFrame([[1,2],[4,5],[7,8]],
    index=['cobra','viper','sidewinder'],
    columns=['max_speed','shield'])
print(dfr)
# you can also print multiple items as a list
print(dfr.loc[['viper','cobra']])
# or use a colon to indicate multiple rows from a range, and then specify a column
print(dfr.loc['cobra':'viper', 'max_speed'])

# you can add new columns by simply defining the name and the calculation
df['new'] = df['Duration'] * df['Number of Weeks']
# you can pass a list of any number of valid columns to the filename
listOfCols = ['Number of Weeks', 'Duration', 'new']
print(df[listOfCols].head(10))
