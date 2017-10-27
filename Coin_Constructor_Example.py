# This is building a constructor for coin objects

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

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

     # destructor function below.  When a coin object is deleted this runs.

    def __del__(self):
        print('Coin Spent!')

# created a Coin object called penny
penny = Coin(rare=True)

# testing if worked
print(penny.color)