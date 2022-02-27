# demonstrating scope in functions

def toPower ( number , power = 3 ) :
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