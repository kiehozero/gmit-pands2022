# a program to assess a filename, and create it if it does not exist

import os.path

def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

filename = input("Enter your filename:")

if not os.path.isfile(filename):
    print("File does not exist")
    with open(filename,"wt") as f:
        initNum = writeNumber(0)
    print(f"File {filename} created")
else:
    print("File exists")