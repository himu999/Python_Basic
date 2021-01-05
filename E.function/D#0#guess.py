# Guessing the age of person

import random as r
secret_age = r.randint(1, 10)
flag = False


def game_fun(guessed_age, secret):
    if guessed_age < secret:
        return "Too low"
    elif guessed_age > secret:
        return "Too high"
    else:
        return "CORRECT!"


for i in range(1, 6):
    print("Take a guess. you have "+str(6-i)+' guess left..')
    guess = int(input())
    if game_fun(guess, secret_age) == 'CORRECT!':
        print('You won the game!')
        flag = True
        break
if not flag:
    print("You lost the game")
