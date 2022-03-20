# most of this will be unworkable, don't try to run it without commenting out everything but the line you need

# SyntaxError
# var = 2 +

# ZeroDivisionError
# zero = 10/0

# FileNotFoundError

file = 'data.txt'
try:
    with open(file) as f:
        print(f.read())
# it is wise to write except statements for particular errors or scenarios to make life easier when debugging
except FileNotFoundError:
    print(f"No file with the name {file} was located")
except:
    print("Some other error")
finally:
    print("This will always be printed")