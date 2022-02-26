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

# appends a list of courses to a blank list
courses = [ ] 
for module in student [ "modules" ] :
    courses.append ( module [ "courseName" ] )

welcome = input ( " Hello {}, please type c to see a list or courses, or q to quit: ".format ( student [ "name" ] ) )

while welcome == "c":
    reqCourse = input ( "Please select a course from the list below, or type q to quit.\n {}:".format ( courses ) )
    if reqCourse != "q":
        try:
            # find the required course as an index value within the list of all courses
            locCourse = courses.index ( reqCourse )
            # prints the course grade
            print ( "Your grade for {} is {}.".format ( reqCourse , student [ "modules" ] [ locCourse ] [ "grade" ] ) )
        except:
            print ( "Course not found. Please try again." )
    else:
        break

print ( "End" )