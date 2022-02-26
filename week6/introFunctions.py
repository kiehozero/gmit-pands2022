# Demonstrating the use of functions, this takes two numbers and multiplies them


def toPower ( number , power = 3 ) :
    # the power above has a default value, if one isn't given in the input below
    # in reality, you can't enter a blank in the inputs below, the above is just
    # to demonstrate the ability to do it.
    print ( number )
    return number ** power

starter = int ( 
    input ( "input a value to cube: " ) 
    )

power = int (
    input ( "input a multiplier : ")
)

print ( 
    toPower ( starter , power ) 
    )