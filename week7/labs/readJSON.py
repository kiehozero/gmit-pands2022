import json
filename = input("Type a file name: ")

def readDict():
    with open(filename) as f:
        return json.load(f)

newDict = readDict()
print(newDict)
