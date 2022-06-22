"""
This module contains operator randomizer, 
arithmetic question, addition, subtraction, 
multiplication operations and the core-function
of the brain_calc.py.
"""

from random import randint

import prompt


def sum(num1, num2):
    return num1 + num2


def diff(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def isPrime(num):
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


def arithmetic_question(num1, num2, operation):
    print('Question: {0} {2} {1}'.format(num1, num2, operation))


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


def uncorrect_answ(answer, correct_answ, name):
    print(
        '"{0}" is wrong answer ;(. Correct answer was "{1}".\nLet\'s try again, {2}!'
        .format(answer, correct_answ, name)
        )


def check(num1, num2, answer, funct, name):
    correct_answ = funct(num1, num2)
    if answer == correct_answ:
            print('Correct!')
    else:
        uncorrect_answ(answer, correct_answ, name)
        return False


def doOperation(name, operator=''):
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    arithmetic_question(num1, num2, operator)
    answer = prompt.integer('Your answer: ')
    if operator == '+':
        result = check(num1, num2, answer, sum, name)
        return result
    elif operator == '-':
        result = check(num1, num2, answer, diff, name)
        return result
    elif operator == '*':
        result = check(num1, num2, answer, mult, name)
        return result
    elif operator == '':
        result = check(num1, num2, answer, gcd, name)
        return result
