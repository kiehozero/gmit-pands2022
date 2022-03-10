# function storage for student input file

import json

filename = "students.json"

def displayMenu ( ) :
    print ( "What would you like to do?")
    print ( "\t (a) Add new student" )
    print ( "\t (v) View students" )
    print ( "\t (s) Save file" )
    print ( "\t (l) Load File" )
    print ( "\t (q) Quit")
    userChoice = input (
        "Type one letter (a/v/s/l/q): "
        )
    return userChoice

def doAdd ( students ) :
    currentStudent = { }
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

def displayModules ( modules ) :
    print ( "\tName\tGrade" )
    for module in modules :
        print ("\t{}\t{}".format ( module [ "name" ] , module [ "grade" ] ) )

def doView ( students ) :
    for currentStudent in students :
        print ( currentStudent [ "name" ] )
        displayModules ( currentStudent [ "modules" ] )

def doLoad ( ) :
    # filename = "students.json"
    # with open ( filename , "r+" ) as f:
    #     return json.load ( f )
    print ("load")

def doSave ( students ) :
    with open ( filename , "wt" ) as f:
        json.dump ( students , f )
    print ( "doSave" )