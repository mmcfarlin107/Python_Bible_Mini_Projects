#Script that randomly selects a question from a baby that you must answer
#The only answer to make the baby be quiet is the simple answer 'just because'

from random import choice

questions = ['Why is the sky blue?: ',
             'Why is the face on the moon?: ',
             'Where are all the dinosaurs?: ']

question = choice(questions)
answer = input(question).strip().lower()

while answer != 'just because':
    answer = input('why? ').strip().lower()

print('oh... okay')