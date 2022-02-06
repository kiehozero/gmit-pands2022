# initial testing of for loops

boats = ['Sigma', 'Beneteau', 'Swam', 99]

for boat in boats:
    print ( "I'd prefer to be out on a " + str ( boat ) )

for number in range ( 1, 10 ):
    square = number * number
    print ( "the square of {} is {} ".format( number , square ) )