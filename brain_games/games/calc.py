"""This game feature tests the user's arithmetic ability."""

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


def calc(iteration_number):
    if iteration_number == 0:
        rules = 'What is the result of the expression?'
    else:
        rules = None
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operator = randomize_operator()
    question = '{0} {2} {1}'.format(number1, number2, operator)
    if operator == '+':
        correct_answer = number1 + number2
        return rules, question, correct_answer
    if operator == '-':
        correct_answer = number1 - number2
        return rules, question, correct_answer
    if operator == '*':
        correct_answer = number1 * number2
        return rules, question, correct_answer
