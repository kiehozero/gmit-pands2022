from unicodedata import name

from paramiko import Agent


class Dog:
    # class attributes can be defined and are the same for all instances of that class, and must contain a value
    species = "Canis Familiaris"

    # all classes must have an init method. This sets the initial state of an object when a new instance is created
    def __init__(self, name, age):
        # init can contain any number of parameters. The value of these parameters are known as attributes once the
        # instance is created. Creating a new object is also known as instantiation.
        self.name = name
        self.age = age

    # classes can also contain methods
    def description(self):
        return f"{self.name} is {self.age} years old."

    def __str__(self):
        return f"{self.name} is {self.age} years old."

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

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