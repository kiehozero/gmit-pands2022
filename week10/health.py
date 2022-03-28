# using the person module

import datetime as dt
from personmodule import *

if __name__ == '__main__':
    person1 = {
            'firstname': 'Andrew', 
            'lastname': 'Saint', 
            'dob': dt.date(1964,12,15),
            'height': 180,
            'weight': 100
        }

displayperson(person1)
gethealthdata(person1)