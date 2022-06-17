"""
This module contains operator randomizer, 
arithmetic question, addition, subtraction, 
multiplication operations and the core-function
of the brain_calc.py
"""

import prompt

from random import randint


def sum(number1, number2):
    return number1 + number2


def diff(number1, number2):
    return number1 - number2


def mult(number1, number2):
    return number1 * number2


def arithmetic_question(number1, number2, operation):
    print('Question: {0} {2} {1}'.format(number1, number2, operation))


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


def doOperation(num1, num2, operator, name):
    arithmetic_question(num1, num2, operator)
    answer = prompt.integer('Your answer: ')
    if operator == '+':
        correct_answ = sum(num1, num2)
        if answer == correct_answ:
            print('Correct!')
        else:
            print(
                '"{0}" is wrong answer ;(. Correct answer was "{1}".\nLet`s try again, {2}'
                .format(answer, num1 + num2, name))
            return False
    elif operator == '-':
        correct_answ = diff(num1, num2)
        if answer == correct_answ:
            print('Correct!')
        else:
            print(
                '"{0}" is wrong answer ;(. Correct answer was "{1}".\nLet`s try again, {2}'
                .format(answer, num1 - num2, name))
            return False
    else:
        correct_answ = mult(num1, num2)
        if answer == correct_answ:
            print('Correct!')
        else:
            print(
                '"{0}" is wrong answer ;(. Correct answer was "{1}".\nLet`s try again, {2}'
                .format(answer, num1 * num2, name))
            return False
