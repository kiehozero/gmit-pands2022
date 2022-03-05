# main program, this is a split of the menuCall file, and all of the functions
# are stored within the studentsUtil.py file as a demonstration of modules.

import studentsUtil as s

students = []
choice = s.displayMenu ( )

while (choice != "q" ) :
    if choice == "a" :
        s.doAdd ( students )
    elif choice == "v" :
        s.doView ( students )
    else:
        print ( "Invalid selection" )
    choice = s.displayMenu ( )
