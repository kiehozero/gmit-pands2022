# following the tutorial at https://realpython.com/python-csv/

import csv

# note that when using writer, you'll need to specify the write mode as an open() parameter
with open("employee_birthday.txt", "w") as f:
    # fieldnames is mandatory when writing a dictionary as it establishes the keys
    fieldnames = ['emp_name', 'dept', 'birth_month']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    # overwrites existing items
    csv_writer.writeheader()
    csv_writer.writerow({'emp_name':'Eilin Grant', 'dept':'Doggos', 'birth_month':'June'})
    csv_writer.writerow({'emp_name':'John Smith','dept':'Accounting','birth_month':'November'})
    csv_writer.writerow({'emp_name':'Erica Meyers','dept':'IT','birth_month':'March'})