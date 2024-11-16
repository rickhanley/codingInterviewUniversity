class Banana:
    """A tasty tropical fruit"""
    food_group = 'fruit'
    colours = [
        'green', 'green-yellow', 'yellow',
        'brown', 'brown-spotted', 'black'
    ]
    
    def peel(self):
        self.peeled = True
        
    def set_colour(self, colour):
        """Set the colour of the banana"""
        if colour in self.colours:
            self.colour = colour
        else:
            raise ValueError (f'A banana cannot be {colour}!')
        
my_banana = Banana()
my_banana.set_colour('green')
# my_banana.peel()

print(my_banana.peeled)
