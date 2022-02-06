# Task: Write a program (grade.py) that reads in a students percentage mark and prints out corresponding the grade.
# The program should check that the percentage is valid:
# • Under 40% => Fail
# • Between 40% and 49% => Pass
# • Between 50% and 59% => Merit 2
# • Between 60% and 69% => Merit 1
# • Over 70% => Distinction

grade = float ( input ( "Enter the percentage: ") )

if ( grade <= 40 ) :
    print( "Fail" )
elif ( grade <= 49 ) :
    print ( "Pass" )
elif ( grade <= 59 ) :
    print ( "Merit 2" )
elif ( grade <= 69 ) :
    print ( "Merit 1" )
else:
    print ( "Distinction" )

# Answer moved the <= 40 statement to elif, and made the initial if statement an error handler to remove anything lower than 0 or over 100