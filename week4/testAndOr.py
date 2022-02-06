# testing with 'and' and 'or'

UserNo = int(input("Enter your number: "))

if ( UserNo >= 0 ) and ( UserNo <= 100 ) :
    print ( "valid" )

if ( UserNo <= 0 ) or ( UserNo >= 100 ) :
    print( "stop" )
else:
    print( "go" )