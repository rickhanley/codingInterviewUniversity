print("hello")

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        
    def details(self):
        print(f"This instance is {self.name} age {self.age}")

names = ["Dave", "Annie", "Charlie", "Barry", "Elliot", "Fedora", "Gill", "Helen", "Ian", "Jakes"]

for x in range(10):
    person = Person(x, names[x])
    person.details()
        