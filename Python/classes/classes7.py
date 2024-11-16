class Banana:
    
    def __str__(self):
        return f'A {self.colour} {self.__class__.__name__}'
    
    def __repr__(self):
        return f"MyClass(value={self.colour})"
    
    food_group = 'fruit'
    colours = [
        'green', 'green-yellow', 'yellow',
        'brown', 'brown-spotted', 'black'
    ]
    
    __ripe_colours = ['yellow', 'brown-spotted']
    
    def _is_ripe(self):
        return self.colour in self.__ripe_colours
    
    def can_eat(self, must_be_ripe=False):
        if must_be_ripe and not self._is_ripe():
            return False
        return True
    
    def peel(self):
        self.peeled = True
        
    def set_colour(self, colour):
        if colour in self.colours:
            self.colour = colour
        else:
            raise ValueError(f'A Banana cannot be {colour}!')
    
    @classmethod
    def check_colour(cls, colour):
        return colour in cls.colours
    
my_banana = Banana()
my_banana.set_colour('green')
my_banana.peel()

print(my_banana)

# print(my_banana.check_colour("Yellow".lower()))
# print(my_banana.colours)