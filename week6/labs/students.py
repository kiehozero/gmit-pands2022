# main program, this is a split of the menuCall file, and all of the functions
# are stored within the studentsUtil.py file as a demonstration of modules.

import studentsUtil as s

students = []

menuChoice = {
    "a" : s.doAdd ,
    "v" : s.doView ,
    "s" : s.doSave ,
}

choice = s.displayMenu ( )

while (choice != "q" ) :
    if choice in menuChoice :
        menuChoice [ choice ] ( students )
    elif choice == "l" :
        students = s.doLoad ( )
    else:
        print ( "Invalid selection" )
    choice = s.displayMenu ( )
