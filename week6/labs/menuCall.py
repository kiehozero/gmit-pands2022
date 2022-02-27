# A program to add students, their modules and grades into a database

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
    students.append ( { "name" : studentName , "modules" : addModule ( ) } )
    addModule ( )

def addModule ( ) :
    modules = [ ]
    modName = input ( "Name of module (leave blank to finish adding modules): " )

    while modName != "" :
        thisModule = {}
        thisModule["name"] = modName
        thisModule["grade"] = int ( input ( "Module grade: " ) )
        modules.append ( thisModule )
        modName = input ( "Name of module (leave blank to finish adding modules): " )

    return modules

def doView ( ) :
    for student in students:
        name = student["name"]
        modules = student["modules"]
        print ( f"Name: {name}" )
        for module in modules:
            modName = modules[0]
            modGrade = modules[1]
            print ( f"{modName}: {modGrade}" )


students = []
choice = displayMenu ( )

while (choice != "q" ) :
    if choice == "a" :
        doAdd ( )
    elif choice == "v" :
        doView ( )
    else:
        print ( "Invalid selection" )
    choice = displayMenu ( )

