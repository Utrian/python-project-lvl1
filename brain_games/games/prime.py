"This module is an implementation of the game \"is it a prime number?\"."

import prompt

from random import randint


def isPrime(num):
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


def prime(name, i):
    if i == 0:
        print(
            'Answer "yes" if given number is prime. '
            'Otherwise answer "no".'
        )
    num = randint(1, 3571)
    print('Question: ' + str(num))
    answer = prompt.string('Your answer: ')
    correct_answer = isPrime(num)
    if answer == 'yes' and correct_answer is True:
        return True
    elif answer == 'no' and correct_answer is False:
        return True
    else:
        if answer == 'yes':
            correct_answer = 'no'
        else:
            correct_answer = 'yes'
        print(
            '"{0}" is wrong answer ;(. Correct answer was "{1}". '
            'Let\'s try again, {2}!'
            .format(answer, correct_answer, name)
        )
        return False
