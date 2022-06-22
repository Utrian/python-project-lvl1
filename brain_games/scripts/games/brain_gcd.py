"""This game tests the user's understanding of finding the GCD."""

from brain_games.cli import welcome_user

import brain_games.oper


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        result = brain_games.oper.doOperation(name)
        if result != False:
            i += 1
        else:
            return
    print("Congratulations, {0}!".format(name))


if __name__=='__main__':
    main()
