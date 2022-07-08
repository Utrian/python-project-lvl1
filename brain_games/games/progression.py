"""
This game asks the user to find
the missing number in an arithmetic
progression.
"""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_correct_answer(length, start, step, hidden_index):
    progression = list(range(start, (start + length * step), step))
    correct_answer, progression[hidden_index] = progression[hidden_index], ".."
    progression = [str(num) for num in progression]
    progression = ' '.join(progression)
    question = 'Question: {0}'.format(progression)
    return question, correct_answer


def progression():
    length = 10
    start = randint(1, 100)
    step = randint(1, 5)
    hidden_index = randint(0, 9)
    return get_question_and_correct_answer(length, start, step, hidden_index)
    


def start():
    return progression()
