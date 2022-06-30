"""
This game tests the user's understanding
of finding the greatest common divisor.
"""

import prompt

from random import randint


def gcd(name, i):
    if i == 0:
        print(
            'Find the greatest common '
            'divisor of given numbers.'
        )
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    print('Question: {0} {1}'.format(num1, num2))
    answer = prompt.integer('Your answer: ')
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    correct_answer = num1 + num2
    if answer == correct_answer:
        return True
    else:
        print(
            '"{0}" is wrong answer ;(. Correct answer was "{1}". '
            'Let\'s try again, {2}!'
            .format(answer, correct_answer, name)
        )
        return False
