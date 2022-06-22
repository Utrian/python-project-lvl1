"""This game feature tests the user's arithmetic ability."""

import brain_games.oper

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        operator = brain_games.oper.randomize_operator()
        result = brain_games.oper.doOperation(name, operator)
        if result is not False:
            i += 1
        else:
            return
    print("Congratulations, {0}!".format(name))


if __name__ == '__main__':
    main()
