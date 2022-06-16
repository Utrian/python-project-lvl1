import prompt

def welcome_user():
    name = prompt.string('Mai I have your name? ')
    print('Hello, {}!'.format(name))
