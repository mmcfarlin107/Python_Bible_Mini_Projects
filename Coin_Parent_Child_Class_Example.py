# This is building a constructor for coin objects.
# Not best example, but used for practice and to have syntax documented

# importing random for flip method
import random


class Coin:
    # constructor function below

    def __init__(self, rare='false'):
        self.rare = rare
        self.color = 'gold'
        self.heads = True

    def rust(self):
        self.color = 'greenish'
        return 'rusted'

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

        # destructor function below.  When a coin object is deleted this runs.

    def __del__(self):
        print('Coin Spent!')



class Nice_Coin(Coin): #by putting 'Coin' as a parameter it is a child class of 'Coin'
    def __init__(self):
        Coin.__init__(self) # Inherit parent values with this command
        self.value = 100000
        self.year = 1854
        self.weight = 1.23
        self.rare = True

#created a nice_coin object called quarter
quarter = Nice_Coin()

print(quarter.weight) #in Nice_Coin constructor itself.
print(quarter.rust()) #inherited from parent class
print(quarter.heads) #inherited from parent class