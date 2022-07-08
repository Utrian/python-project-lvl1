"This module is an implementation of the game \"is it a prime number?\"."

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number and number % divisor != 0:
        divisor += 2
    return divisor * divisor > number


def get_question_and_correct_answer():
    number = randint(1, 3571)
    question = 'Question: {0}'.format(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
