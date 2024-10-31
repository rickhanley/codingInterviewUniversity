class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def summary(self):
        print("Name: ", self.name, ", Age: ", self.age)
        

me = Person("Rick", "48")

me.summary()