"""This game is for understending even and odd numbers."""

from random import randint


def even(iteration_number):
    if iteration_number == 0:
        rules = "Answer 'yes' if the number is even, otherwise answer 'no'."
    else:
        rules = None
    number = randint(1, 100)
    question = str(number)
    if number % 2 == 0: correct_answer = 'yes'
    else: correct_answer = 'no'
    return rules, question, correct_answer
