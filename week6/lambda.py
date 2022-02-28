# introduction to anonymous functions, lambdas replace below functions

# def doubler ( num ) :
#     return num * 2

# def tripler ( num ) :
#     return num * 3

isMax = True

if isMax:
    fun = lambda num : num * 2
else:
    fun = lambda num : num * 3

var = fun ( 10 )

print ( var )