"""This game is for understending even and odd numbers."""

from random import randint

DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."


def get_question_and_correct_answer(number):
    question = 'Question: {0}'.format(str(number))
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def even():
    number = randint(1, 100)
    return get_question_and_correct_answer(number)


def start():
    return even()
