"""
This game asks the user to find
the missing number in an arithmetic
progression.
"""

import prompt

from random import randint


def progression(name, i):
    if i == 0:
        print('What number is missing in the progression?')
    start_number = randint(1, 100)
    next_number = start_number
    arith_progression = ''
    step = randint(1, 5)
    miss = randint(1, 10)
    j = 1
    while j != 11:
        if j != miss:
            next_number += step
            arith_progression = (
                arith_progression + " " + str(next_number)
            )
            j += 1
        else:
            next_number += step
            correct_answ = next_number
            arith_progression = (
                arith_progression + " " + ".."
            )
            j += 1
    print('Question:' + arith_progression)
    answ = prompt.integer('Your answer: ')
    if answ == correct_answ:
        return True
    else:
        print(
            '"{0}" is wrong answer ;(. Correct answer was "{1}". '
            'Let\'s try again, {2}!'
            .format(answ, correct_answ, name)
        )
        return False
