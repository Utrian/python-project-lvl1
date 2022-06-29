"""This game is for understending even and odd numbers."""

import prompt

from random import randint


def even(name, i):
    if i == 0: 
        print(
        "Answer 'yes' if the number is even, "
        "otherwise answer 'no'."
        )
    num = randint(1, 100)
    print('Question: ' + str(num))
    answer = prompt.string('Your answer: ')
    if num % 2 == 0 and answer == "yes":
        return True
    elif num % 2 != 0 and answer == "no":
        return True
    else:
        if answer == 'yes':
            correct_answer = 'no'
        else:
            correct_answer = 'yes'
    print(
        '"{0}" is wrong answer ;(. Correct answer was "{1}". '
        'Let\'s try again, {2}!'
        .format(answer, correct_answer, name)
    )
    return False
