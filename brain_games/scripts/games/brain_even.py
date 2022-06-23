"""This game is for understending even and odd numbers."""

from random import randint

from brain_games.cli import welcome_user


def main():
    """Let`s start."""
    i = 0
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    while i < 3:
        number = randint(0, 100)
        print("Question: " + str(number))
        answer = input("Your answer: ")
        if number % 2 == 0 and answer == "yes":
            print("Correct!")
            i += 1
        elif number % 2 != 0 and answer == "no":
            print("Correct!")
            i += 1
        elif number % 2 == 0 and answer == "no":
            print(
                "'no' is wrong answer ;(. "
                "Correct answer was 'yes'."
                "\nLet's try again, {0}!".format(name)
                )
            return
        else:
            print(
                "'yes' is wrong answer ;(. "
            "Correct answer was 'no'."
            "\nLet's try again, {0}!".format(name)
            )
            return
    print("Congratulations, {0}!".format(name))


if __name__ == '__main__':
    main()
