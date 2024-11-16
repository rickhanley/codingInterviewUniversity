

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
my_person = Person("Rick", 48)

class PersonPlus(Person):
    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation
        

print(f"{my_person.name} is {my_person.age} years old")

my_person_plus = PersonPlus("Rick", 48, "Senior Grants Officer")

print(f"{my_person_plus.name} is {my_person_plus.age} years old and woprks as a {my_person_plus.occupation}")