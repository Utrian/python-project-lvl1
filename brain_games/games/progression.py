"""
This game asks the user to find
the missing number in an arithmetic
progression.
"""

import prompt

from random import randint


def progression(iteration_number):
    if iteration_number == 0:
        rules = 'What number is missing in the progression?'
    else: 
        rules = None
    start_number = randint(1, 100)
    next_number = start_number
    arith_progression = ''
    step = randint(1, 5)
    skip_number = randint(1, 10)
    iteration_counter = 1
    while iteration_counter != 11:
        if iteration_counter != skip_number:
            next_number += step
            arith_progression = (
                arith_progression + " " + str(next_number)
            )
            iteration_counter += 1
        else:
            next_number += step
            correct_answ = next_number
            arith_progression = (
                arith_progression + " " + ".."
            )
            iteration_counter += 1
    question = arith_progression
    return rules, question, correct_answ
