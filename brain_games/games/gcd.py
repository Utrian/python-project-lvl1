"""
This game tests the user's understanding
of finding the greatest common divisor.
"""

from random import randint


def gcd(iteration_number):
    if iteration_number == 0:
        rules = 'Find the greatest common divisor of given numbers.'
    else: 
        rules = None
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = '{0} {1}'.format(number1, number2)
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    correct_answer = number1 + number2
    return rules, question, correct_answer
