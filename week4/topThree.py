# generate 10 random numbers, return the three highest numbers

import random

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

randNum = []

for i in range ( 0 , 10 ):
    randNum.append( random.randint( rangeFrom, rangeTo ) )

print ( randNum )
topOnes = randNum.copy()
topOnes.sort(reverse=True)
print ("The top {} are \t\t {}".format ( topHowMany , topOnes [ 0:topHowMany ] ) )