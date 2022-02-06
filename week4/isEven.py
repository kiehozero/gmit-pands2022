# Task: Write a program (isEven.py) that asks the user to enter in a number, and the program will tell the user if the number is even or odd.

userNo = int ( input ( "Enter a number: " ) )

if ( userNo % 2 ) == 0:
    print ( "{} is an even number.".format ( userNo ) )
else:
    print ( "{} is an odd number.".format ( userNo ) )