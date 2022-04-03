import pandas as pd

dataAsDictOfList = {
    "Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22,35,58],
    "Sex": ["male", "male", "female"],
}

# DataFrame can take an additional argument as an index
df = pd.DataFrame(dataAsDictOfList,index=["a","b","c"])

print(df)

# describe gives a statistical summary of numerical columns
print(df.describe())

dataAsDictOfDict = {
    "Name": {
        "101": "Braund, Mr. Owen Harris",
        "102": "Allen, Mr. William Henry",
        "104": "Bonnell, Miss. Elizabeth",
    },
    "Age": {"101": 22, "102": 35, "104": 58},
    "Sex": {"101": "male", "102": "male", "104": "female"},
}

print(dataAsDictOfDict)

dataAsLists = [[1,2,100,"male"],
    [2,4,100,"male"],
    [3,8,100,"female"]]

df = pd.DataFrame(dataAsLists,columns=["x","y","percent","sex"])

print(df)