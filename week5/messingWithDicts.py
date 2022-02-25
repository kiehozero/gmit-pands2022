make = "ford"
model = "mondeo"
year = 2006
owner = "andrew"

# causes issues once you want to store more than one vehicle

car = {
    "make" : "ford" ,
    "model" : "mondeo" ,
    "year" : 2006 ,
    "owner" : {
        "name" : "andrew" ,
        "number" : "1123"
    } ,
    "tags" : ["pre-owned", "needs tlc", "certified seller"]
}

print ( car [ "owner" ] [ "name" ] )
# get will return a value if the key is present, but won't throw an error if it isn't present
print ( car.get ( "registration" ) )
# keys returns the keys in the dictionary as a List, values does the same for the second part of the pair
print ( car.keys ( ) )
print ( car [ "owner" ].keys ( ) )
# items will return each key-value pair as a Tuple within a List
print ( car.items ( ) )

for x, y in car.items ( ) :
    print ( x , y )

for key in car:
    print ( key , "is" , car[key] )