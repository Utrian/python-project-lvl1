from brain_games.cli import welcome_user
from random import randint

def isPrime(num):
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num

print(isPrime(6))

