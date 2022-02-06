rightNum = 30

guess = int ( input ( "Please guess the number: " ) )

while guess != rightNum:
    print ( "Wrong" )
    if guess < rightNum:
        guess = int ( input ( "Too low, please guess again: " ) )
    else: 
        guess = int ( input ( "Too high, please guess again: "))

print ( "Well done! The correct number is {}.".format ( rightNum ) )