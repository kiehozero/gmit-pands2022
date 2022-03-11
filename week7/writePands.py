# from the RealPython tutorial https://realpython.com/python-csv/

import pandas as pd

df = pd.read_csv(
    'hrdata.csv',
    index_col='Employee',
    parse_dates=['Hired'],
    header=0,
    names=['Employee', 'Hired', 'Salary', 'Sick Days']
    )

df.to_csv('hrdata copy.csv')

print("Write complete")