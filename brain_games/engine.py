"""
This module contains the basis
for the operation of the "mind game".
"""


def run_game(game):
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print("Hello, {0}!".format(name))
    for iteration_number in range(3):
        rules, question, correct_answer = game(iteration_number)
        if iteration_number == 0: print(rules, 'Question: ' + question.strip(), sep='\n')
        else: print('Question: ' + question.strip())
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(
                '"{0}" is wrong answer ;(. Correct answer was "{1}". '
                'Let\'s try again, {2}!'
                .format(answer, correct_answer, name)
            )
            return
    print("Congratulations, {0}!".format(name))
