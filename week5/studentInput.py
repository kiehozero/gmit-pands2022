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

courses = [ ]
for module in student["modules"]:
    courses.append ( module [ "courseName" ] )
requiredCourse = input ( "Enter a module from the following list:\n{}: ".format ( courses ) )
print(courses)
print(requiredCourse)
# for x, y in student [ "modules" ][ requiredCourse ] :
#     print ( "\t {} \t: {}".format ( module [ "courseName" ] , module [ "grade" ] ) )