# following the tutorial at https://realpython.com/python-csv/

import csv

with open("employee_birthday.txt") as f:
    # csv.DictReader returns each row as a dictionary, it assumes the first row are keys
    # if the file doesn't contain keys, you can set a list variable and refer to it in
    #DictReader using the fieldnames parameter
    csv_reader = csv.DictReader(f)
    line_count = 0
    for row in csv_reader:
        line_count += 1
        print(row)
    print(f'Number of data rows: {line_count}')