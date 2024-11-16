class Car():
    def __init__(self, colour, chassis):
        self.colour = colour
        self.chassis = chassis
    
    def info(self):
        print(f"{self.colour} {self.chassis}")

my_car = Car("Grey", "Estate")

my_car.info()