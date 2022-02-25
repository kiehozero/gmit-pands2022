# Write a program that will read in the data for the data structure above, ie
# reads in a student’s name, then keeps reading in their modules and grades (until 
# the user enters a blank module name). You can break this up into two parts:
#   a. Just read in the module names until the user enters blank,
#   b. Then read in the grade as well
# This program can just read in one student (and their module details).

student = {
    "name" : "Mary" ,
    "modules" : 
    [ { 
        "courseName" : "Programming" ,
        "grade" : 45
    } ,
    { 
        "courseName" : "History" ,
        "grade" : 99
    } ]
}

input("Enter a module: ")

print ( "Student: {}".format ( student [ "name" ] ) )
for module in student ["modules" ] :
    print ("\t {} \t: {}".format( module [ "courseName" ], module ["grade"] ) )