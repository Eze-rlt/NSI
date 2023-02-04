from random import randint
from os import system

def clear():
    system('cls')

clear()
secret_nbe = randint(1, 100)
bigger = 100
taller = 0
user_nbe = -1

while user_nbe!=secret_nbe:
    print(f'{taller} < secret < {bigger}')
    user_nbe = int(input('Quel est votre nombre ? '))
    
    clear()
    if user_nbe<secret_nbe:
        taller = user_nbe
        print('Plus grand !!')
    elif user_nbe>secret_nbe:
        bigger = user_nbe
        print('Plus petit !!')


input('Bravo, vous avez gagnés !!! ')