# how to read one line at a time, this would be useful
# when you want to read lines until a certain point using
# a for loop, or printing lines selective using an if loop 

with open("introFiles.py") as i:
    # l variable generates a line counters
    l = 0
    for line in i:
        l += 1
        # index ref below removes the final character of
        # each line, which is always the carriage return
        print(l, line[:-1])