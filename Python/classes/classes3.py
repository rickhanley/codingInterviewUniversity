class Person:
    def __init__(self, name , age):
       self.name = name
       self.age = age
       
    def details(self):
        print("Details: ", self.name, ", ", self.age)
        

me = Person("Rick", 48)

me.details()