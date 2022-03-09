# using the built-in os module that interacts with the operating system
# this is useful if you want to delete (the .remove() function) files, 
# check whether or not the file or folder exists (the .exists() function).

import os, pandas

filename = input("Please enter a filename: ")
l = 0

if os.path.exists(filename):
    print (filename, "already exists.")
    choice = input("Do you want to open the file? \ny for yes\nd to delete\nany key to quit\n")
    if choice == "y":
        with open(filename) as i:
            l = 0
            for line in i:
                l += 1
                # bug here, if the file is only one line long, it will
                # skip the last character as there is no carriage break
                print(l, line[:-1])
    elif choice == "d":
        # add failsafe message here
        os.remove(filename)
    else:
        print("End")
        
else:
    createChoice = input(f"{filename} does not exist. Do you want to create it? \nw to create\nany key to quit\n")
    if createChoice == "w":
        with open(filename,"wt") as f:
            userText = input("Write your text: ")
            f.write(userText)
    else:
        print("End")