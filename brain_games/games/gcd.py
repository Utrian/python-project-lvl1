"""
This game tests the user's understanding
of finding the greatest common divisor.
"""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_greatest_common_divisor(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return number1 + number2


def get_question_and_correct_answer():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    question = f'{number1} {number2}'
    return question, str(get_greatest_common_divisor(number1, number2))
