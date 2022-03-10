# a program that counts how many times a program has run and prints it to the file

filename = "count.txt"

def readNumber():
    with open(filename, "rt") as f:
        count = int(f.read())
        return count

def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

newCount = readNumber() + 1
writeNumber(newCount)
print(newCount)
