# Creating a health potion for an imaginary game in Python
#The harder the difficulty, the less health you get on average.

import random

health = 50
# for difficulty below, 1 is easy, 2 is medium, 3 is hard
difficulty = 1

potion_health = int(random.randint(25, 50)/difficulty)

health += potion_health

print(health)