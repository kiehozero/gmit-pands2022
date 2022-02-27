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
    # press a
    pass

def doView ( ) :
    # press v
    pass

choice = displayMenu ( )
print ( f"You chose {choice}" )