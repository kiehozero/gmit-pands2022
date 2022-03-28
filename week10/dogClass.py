class Dog:
    # class attributes can be defined and are the same for all instances of that class, and must contain a value
    species = "Canis Familiaris"

    # all classes must have an init method. This sets the initial state of an object when a new instance is created
    def __init__(self, name, age, breed):
        # init can contain any number of parameters. The value of these parameters are known as attributes once the
        # instance is created. Creating a new object is also known as instantiation.
        self.name = name
        self.age = age
        self.breed = breed

    # classes can also contain methods
    def description(self):
        return f"{self.name} is {self.age} years old."

    def __str__(self):
        return f"{self.name} is {self.age} years old."


# this will be a child class of Dog
class SharPei(Dog):
    # __init__ will override the parent __init__, so you need to call that to bring it in as well and also bring in new items
    def __init__(self, name, age, breed, color):
        Dog.__init__(self, name, age, breed)
        self.color = color

class GoldenRetriever(Dog):
    pass

class Boxer(Dog):
    pass

buddy = GoldenRetriever("Buddy", 9, "Golden Retriever")
dixie = SharPei("Dixie", 6, "Shar Pei", "Blue")
miles = Boxer("Miles", 4, "Boxer")



# below will print the memory location of the item if the __str__ method is not included in the class. The output 
# would read: "<__main__.Dog object at 0x000001FE86095BB0>"
print(buddy)
# use dot notation to print particular instance attributes
print(miles.age)
# this also works with class attributes
print(miles.species)

# below prints a class method
print(miles.description())
# this is identical to the above, using __str__ allows you to manipulate the default value that is returned
print(miles)
print(dixie.color)