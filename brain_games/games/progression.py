"""
This game asks the user to find
the missing number in an arithmetic
progression.
"""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_correct_answer():
    amount_numbers = 10
    first_number = randint(1, 100)
    step = randint(1, 5)
    hidden_index = randint(0, 9)

    progression = list(range(first_number,
                            (first_number + amount_numbers * step),
                            step)
                            )
    correct_answer, progression[hidden_index] = progression[hidden_index], ".."
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
