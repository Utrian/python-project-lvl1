"""This game feature tests the user's arithmetic ability."""

import operator

import random


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_correct_answer(number1, number2, operation, func):
    question = 'Question: {0} {2} {1}'.format(number1, number2, operation)
    correct_answer = str(func(number1, number2))
    return question, correct_answer


def calc():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operation = random.choice(list(operations.keys()))
    function_operation = operations[operation]
    return get_question_and_correct_answer(
        number1, number2, operation, function_operation
    )


def start():
    return calc()
