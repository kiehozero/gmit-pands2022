rightNum = 30

guess = int ( input ( "Please guess the number: " ) )

while guess != rightNum:
    print ( "Wrong" )
    guess = int ( input ( "Please guess again: " ) )
    # originally failed to work because I had converted the initialised guess as an int 
    # but not the guess inside the loop, so I was changing the variable to a string

print ( "Well done! The correct number is {}.".format ( rightNum ) )