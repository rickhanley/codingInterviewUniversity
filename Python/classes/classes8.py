class Car():
    def __init__(self, model, make):
        self.model = model
        self.make = make
        
class CarInfo(Car):
    def __init__(self, *args):
        args = self.review
        super().__init__(*args)