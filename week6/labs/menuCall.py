def displayMenu ( ) :
    print ( "What would you like to do?")
    print ( "\t (a) Add new student" )
    print ( "\t (v) View students" )
    print ( "\t (q) Quit")
    userChoice = input (
        "Type one letter (a/v/q): "
        )
    return userChoice

def doAdd ( ) :
    studentName = input ( "Type the student's name and press enter: ")
    students.append ( { "name" : studentName , "modules" : [ ] } )

def doView ( ) :
    print ( "This will be a list of students" )
    print ( students )


choice = displayMenu ( )
students = []

while (choice != "q" ) :
    if choice == "a" :
        doAdd ( )
    elif choice == "v" :
        doView ( )
    else:
        print ( "Invalid selection" )
    choice = displayMenu ( )

