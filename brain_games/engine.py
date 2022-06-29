"""
This module contains the basis
for the operation of the "mind game".
"""

import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, {0}!".format(name))
    i = 0
    while i < 3:
        result = game(name, i)
        if result:
            print('Correct!')
            i += 1
        else:
            return 
    print("Congratulations, {0}!".format(name))
