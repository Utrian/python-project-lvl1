"""Greets the user by name."""

import prompt


def welcome_user():
    """Greets the user by name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, {0}!".format(name))
    return name
