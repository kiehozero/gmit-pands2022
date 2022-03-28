from matplotlib.font_manager import _Weight


class Person:
    def __init__(self, firstname, lastname, dob, height, weight):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.height = height
        self.weight = weight
    
    def gethealthstats(self):
        pass

    def display(self):
        print(self)
