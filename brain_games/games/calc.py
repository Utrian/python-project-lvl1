"""This game feature tests the user's arithmetic ability."""

import prompt

from random import randint


def randomize_operator():
    sum = [0, '+']
    diff = [1, '-']
    mult = [2, '*']
    operator = randint(0, 2)
    if operator == 0:
        return sum[1]
    elif operator == 1:
        return diff[1]
    else:
        return mult[1]


def check_answer(answer, correct_answer, name):
    if answer == correct_answer:
        return True
    else:
        print(
            '"{0}" is wrong answer ;(. Correct answer was "{1}". '
            'Let\'s try again, {2}!'
            .format(answer, correct_answer, name)
        )
        return False


def calc(name, i):
    if i == 0:
        print('What is the result of the expression?')
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = randomize_operator()
    print('Question: {0} {2} {1}'.format(num1, num2, operator))
    answer = prompt.integer('Your answer: ')
    if operator == '+':
        correct_answer = num1 + num2
        return check_answer(answer, correct_answer, name)
    if operator == '-':
        correct_answer = num1 - num2
        return check_answer(answer, correct_answer, name)
    if operator == '*':
        correct_answer = num1 * num2
        return check_answer(answer, correct_answer, name)
