"""This game feature tests the user's arithmetic ability."""

import operator

import random


DESCRIPTION = 'What is the result of the expression?'


def get_operation_and_its_function():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operation = random.choice(list(operations.keys()))
    function_operation = operations[operation]
    return operation, function_operation


def get_question_and_correct_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    operation, function_operation = get_operation_and_its_function()
    question = f'{number1} {operation} {number2}'
    correct_answer = str(function_operation(number1, number2))
    return question, correct_answer
