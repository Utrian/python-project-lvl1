from unicodedata import name
from brain_games.cli import welcome_user

from brain_games.oper import isPrime, uncorrect_answ

from random import randint

import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3: 
        num = randint(1, 3571)
        print('Question: ' + str(num))
        answer = prompt.string('Your answer: ')
        correct_answ = isPrime(num)
        if answer == 'yes' and correct_answ == True:
            print('Correct!')
            i += 1
        elif answer == 'no' and correct_answ == False:
            print('Correct!')
            i += 1
        else:
            if correct_answ == True:
                uncorrect_answ(answer, 'yes', name)
            else:
                uncorrect_answ(answer, 'no', name)
            return
    print("Congratulations, {0}!".format(name))


if __name__=='__main__':
    main()