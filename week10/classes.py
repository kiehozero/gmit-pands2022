from unicodedata import name

from more_itertools import last


class Nameofclass:
    name = ""
    last = ""
    
    def getfullname(self):
        return self.name + ' ' + self.last

inst = Nameofclass()
inst2 = Nameofclass()

inst.name = 'Andrew'
inst.last = 'Bloggs'
inst2.last = 'Beatty'
person = inst

print(person.getfullname())

str1 = 'blah de blah'
str2 = str1

str1 += 'ffdsafdas'

print(str2)