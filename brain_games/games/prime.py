"This module is an implementation of the game \"is it a prime number?\"."

from random import randint


def isPrime(number):
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number and number % divisor != 0:
        divisor += 2
    return divisor * divisor > number


def prime(iteration_number):
    if iteration_number == 0:
        rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    else: 
        rules = None
    number = randint(1, 3571)
    question = str(number)
    correct_answer = isPrime(number)
    if correct_answer: correct_answer = 'yes'
    else: correct_answer = 'no'
    return rules, question, correct_answer
