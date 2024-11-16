class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class PersonPlus(Person):
    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation
    def info(self):
        print(f"{self.name} is {self.age} years old and works as a {self.occupation}")
            
MyPerson = PersonPlus("Rick", 47, "Senior Grants Officer")
MyPerson.info()