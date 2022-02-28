# sort list

list = [ 22 , 33 , 11 , 1 , 44 ]
print ( list )

newList = sorted ( list )
print ( newList )

# sort dict

data = [
    { 'first' : 'Mark' , 'last' : 'Jones' , 'YOB' : 1984 } ,
    { 'first' : 'Luke' , 'last' : 'Jones' , 'YOB' : 1975 } ,
    { 'first' : 'John' , 'last' : 'Jones' , 'YOB' : 1986 } ,
]

# function below replaced by lambda
# def sortFun ( item ) :
#     return item [ 'first' ]

print ( data )

# the key below is a parameter of the sorted function, where a function can be used as a key
newData = sorted (
    data , key = lambda item : item [ 'first' ]
    )

print ( newData )