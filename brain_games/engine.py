"""
This module contains the basis
for the operation of the "mind game".
"""

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name? ')
    print(f"Hello, {user_name}!")
    return user_name


def run_game(game):
    rounds_count = 3

    user_name = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(rounds_count):
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(
                f'"{user_answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}". '
                f'Let\'s try again, {user_name}!'
            )
            return
        print('Correct!')
    print(f"Congratulations, {user_name}!")
