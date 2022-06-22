"""
This game asks the user to find
the missing number in an arithmetic 
progression.
"""

from brain_games.cli import welcome_user

from brain_games.oper import uncorrect_answ

from random import randint

import prompt

def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        start_number = randint(1, 100)
        next_number = start_number
        arith_progression = ''
        step = randint(1, 5)
        miss = randint(1, 10)
        j = 1
        while j != 11:
            if j != miss:
                next_number += step
                arith_progression = (
                    arith_progression + " " + str(next_number)
                )
                j += 1
            else:
                next_number += step
                correct_answ = next_number
                arith_progression = (
                    arith_progression + " " + ".."
                )
                j += 1
        print('Question:' + arith_progression)
        answ = prompt.integer('Your answer: ')
        if answ == correct_answ:
            print('Correct!')
            i += 1
        else:
            uncorrect_answ(answ, correct_answ, name)
            return
    print("Congratulations, {0}!".format(name))


if __name__=='__main__':
    main()
