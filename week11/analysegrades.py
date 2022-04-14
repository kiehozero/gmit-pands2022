# in this program I do some basic analysis of the grades.csv
# author: Andrew Beatty

import pandas as pd
import matplotlib.pyplot as plt

filenameForGrades = 'grades.csv'

# there is an index col in this csv, this is not mandatory but will be provided automatically by some data feeds
df = pd.read_csv(filenameForGrades, index_col=0)

# get rid of nulls and duplicates
# we could have chained these calls
# df = df.dropna().drop_duplicates()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# select the highest grade for each subject for a student
df = df.pivot_table(values='grade',index=['name','subject'],aggfunc='max').reset_index()
print(df)

# group by a value in a column. Mean is a standard statistical function in python, you can also use min, max, etc.
meanValues = df.groupby('name').mean()
print(meanValues)

# re-structures the data into the format required to properly populate the graph
df = df.pivot(index='name',columns='subject',values='grade')

# print a correlation table, this is fairly rudimentary for this particular dataset but illustrates the basics 
print(df.corr())


# plot a bar graph
df.plot.bar()

# if you want to plot a sub-set of the dataframe then just select the parts you want to plot, e.g.:
# df[['math', 'SIEM']].plot.bar()

plt.show()
