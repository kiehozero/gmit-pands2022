numList = []

addNum = int ( input ( "Enter number (or 0 to quit): " ) )

while addNum != 0 :
    numList.append ( addNum )
    addNum = int ( input ( "Enter number (or 0 to quit): " ) )

for num in numList :
    print ( num )

average = float ( sum ( numList ) ) / len ( numList )
print ( "The average is {}".format ( average ))