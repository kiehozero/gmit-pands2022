# initial testing of while loops

count = 0

while count < 10 :
    print ( count )
    count += 1

while count >= 0 :
    print ( count )
    count -= 1
print ("blast off!")

val = input ( "enter something (or 'q' to quit): ")

while val != "q" :
    print ( "you said" + val)
    val = input ( "(q to quit): ")