# Opening a file - the two parts of the open function are the path and the mode, always use the below
# method where something is opened inside a with statement

# From w3: There are four different methods (modes) for opening a file:
#    "r"    Read            Default value. Opens a file for reading, error if the file does not exist;
#    "r+"   Read and Write  Opens a file for reading and write, error if the file does not exist;
#    "a"    Append          Opens a file for appending, creates the file if it does not exist;
#    "w"    Write           Opens a file for writing, creates the file if it does not exist;
#    "x"    Create          Creates the specified file, returns an error if the file does exist.

# In addition you can specify if the file should be handled as binary or text mode
#    "t"    Text            Text mode, this is the default;
#    "b"    Binary          Binary mode (e.g. images).

# Functions for dealing with the data are:
#    read() to read in data
#    readline() for a particular line
#    write(somedata) to write in given value
#    seek(offset) to move to a location in a file

filename = "test.csv"

# you can add a full filepath or use dot notation to specify a particular file path

with open(filename,"wt") as f:

    f.write("it's alive!")

with open(filename,"r") as f:

    living = f.readline()
    print(living)
