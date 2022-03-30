class Person:
    # having an init forces us to add the required parameters for a class upon creation
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def fullname(self):
        if hasattr(self, 'middlename'):
            return self.firstname + " " + self.middlename + " " + self.lastname
        else:
            return self.firstname + " " + self.lastname

    # the dunder __str__ provides a default value if the instance is called without any parameters or functions specified
    def __str__(self):
        return self.fullname()

    def addmiddlename(self, middlename):
        self.middlename = middlename

if __name__ == "__main__":
    person1 = Person("Eilin", "Grant")
    print(person1.firstname)

    print(person1.fullname())

    person1.addmiddlename("Joe")
    print(person1)
    