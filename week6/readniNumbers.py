# a program to multiply two numbers together, which will catch input errors

try: 
    num1 = int ( input ( "Enter a number: " ) )
except ValueError:
    num1 = int ( input ( "Numbers only please: " ) )

try: 
    num2 = int ( input ( "Enter another number: " ) )
except ValueError:
    num2 = int ( input ( "Numbers only please: " ) )

answer = num1 * num2

print ( "{} multiplied by {} is {}".format ( num1 , num2 , answer ) )