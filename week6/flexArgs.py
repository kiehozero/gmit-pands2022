# explanation of flexible number of arguments

def flex1 ( *args ) :
    print ( type ( args ) )
    for x in args :
        print ( 
            x , type ( x ) 
            )


flex1 ( "hi" , 55 , 343 , [ ] , { } )


# brief intro to kwargs, which returns as a dictionary instead of a list

def flex2 ( **kwargs ):
    print ( 
        type ( kwargs ) 
        )
    for key, value in kwargs.items():
        print ( f"{ key } is { value } ")

flex2 ( age = 23 , name = "Rooney" , position = "Striker" )

# using a function to accept a flexible range

def average ( *args ):
    sumOfNumbers = sum ( args )
    length = len ( args )
    # can return multiple values, as below
    return sumOfNumbers / length, sumOfNumbers

print ( 
    average ( 2 , 3 , 4 ) 
    )