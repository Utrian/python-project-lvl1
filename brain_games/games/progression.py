"""
This game asks the user to find
the missing number in an arithmetic
progression.
"""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_correct_answer():
    LENGTH = 10
    start = randint(1, 100)
    step = randint(1, 5)
    hidden_index = randint(0, 9)

    progression = list(range(start, (start + LENGTH * step), step))
    correct_answer, progression[hidden_index] = progression[hidden_index], ".."
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
