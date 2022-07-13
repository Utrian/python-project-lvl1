"""
This module contains the basis
for the operation of the "mind game".
"""

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name? ')
    print("Hello, {0}!".format(user_name))
    return user_name


def run_game(game):
    AMOUNT_ROUNDS = 3

    user_name = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(AMOUNT_ROUNDS):
        question, correct_answer = game.get_question_and_correct_answer()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            print(
                '"{0}" is wrong answer ;(. Correct answer was "{1}". '
                'Let\'s try again, {2}!'
                .format(answer, correct_answer, user_name)
            )
            return
    print("Congratulations, {0}!".format(user_name))
