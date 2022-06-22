#!/home/paul/python-project-lvl1/python-project-lvl1/.venv/bin/python3

"""Docestring for linter."""

from brain_games.cli import welcome_user
from scripts.brain_even import even_game


def main():
    """Point of entry."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
