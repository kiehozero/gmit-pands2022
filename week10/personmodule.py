# Demonstration of a module
import datetime as dt

def gethealthdata(person):
    print("get", person['firstname'])

def displayperson(person):
    print(person)

if __name__ == "__main__":
    person1 = {
        'firstname': 'Andrew', 
        'lastname': 'Saint', 
        'dob': dt.date(1964,12,15),
        'height': 180,
        'weight': 100
    }

displayperson(person1)
gethealthdata(person1)