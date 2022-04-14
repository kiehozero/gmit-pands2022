import pandas as pd
from regex import D
listData = [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIEM', 57],
    ['Mark', 'programming', 70],
    ['Mark', 'math', 73],
    ['John', 'programming', 61]
]

df = pd.DataFrame(listData,columns=['name', 'subject', 'grade'])

print(df.head(3))

dfdesc = df.describe()

print(dfdesc)

print(type(dfdesc))

csvFile = "grades.csv"

# df.to_csv(csvFile)

xlsxFile = "grades.xlsx"

# you don't actually need to specify excel_writer below as the parameter, it would be sufficient just to give the variable containing the desired filename, e.g.
# df.to_excel(xlsxFile, sheet_name="data", index=False)
df.to_excel(excel_writer=xlsxFile, sheet_name="data", index=False)

with pd.ExcelWriter(xlsxFile, engine="openpyxl", mode="a") as writer:
    dfdesc.to_excel(writer, sheet_name="summary")

mean = df.describe().loc['mean','grade']

print(mean)