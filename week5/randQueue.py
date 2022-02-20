import random

queue = [ ]

for i in range ( 1 , 11 ) :
    randNum = random.randint ( 1 , 101 )
    queue.append ( randNum )

print ( "queue is ".format ( queue ) )

while len ( queue ) != 0 :
    curNum = queue.pop ( 0 )
    print ( "current number is {} and the queue is {}".format ( curNum , queue ) )

print ( "The queue is now empty" )