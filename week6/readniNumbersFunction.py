# a program to multiply two numbers together, which will catch input errors
# re-factors the similarly-named file to utilise a function and cut down on
# repitition, and also demonstrates entering default and non-default
# arguments into a function

def readNum ( message = "Enter a number: "):
    num = False
    while ( not num ) :
        try :
            num = int ( input ( message ) )
        except ValueError :
            print ( "Please enter numbers only: " , end = "" )
    return num
    
num1 = readNum ( )
num2 = readNum ( "Enter a another number: " )

answer = num1 * num2

print ( f"{num1} multiplied by {num2} is {answer}" )