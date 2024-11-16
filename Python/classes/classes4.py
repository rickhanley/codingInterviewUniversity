class Car():
    group = "vehicle"
    def __init__(self, name):
        self.name = name 
    def info(self):
        print(f"Hello, {self.name} you drive a {self.group}")

my_car = Car("Rick")

my_car.info()

my_car.model = "Honda"

print(my_car.model)