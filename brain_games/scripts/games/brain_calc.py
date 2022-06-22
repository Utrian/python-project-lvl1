"""This game feature tests the user's arithmetic ability."""

from random import randint

from brain_games.cli import welcome_user

import brain_games.oper


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        operator = brain_games.oper.randomize_operator()
        result = brain_games.oper.doOperation(num1, num2, operator, name)
        if result != False:
            i += 1
        else:
            return
    print("Congratulations, {0}!".format(name))

if __name__ == '__main__':
    main()
