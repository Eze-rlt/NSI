from os import system
from random import randint

class colors:
    system('')
    yellow = '\33[93m'
    red = '\33[91m'
    grey = '\33[90m'
    no = '\33[0m'
def reset_grille():
    global grille
    grille = [[None for s in range(6)] for x in range(7)]

grille = list
reset_grille()

def clear():
    system('cls')

def place_jeton(x: int, joueur: int):
    jeton = '0' if joueur == 1 else 'X'
    x-=1

    if grille[x][0] != None:
        return False
    
    for y in range(6):
        y = 6-y-1
        if grille[x][y] == None:
            grille[x][y] = jeton
            break
    return grille

def print_grille():
    for x in range(6):
        print(colors.grey+'|', end=colors.no)
        for y in range(7):
            if grille[y][x] == None:
                print(' ', end=colors.no)
            elif grille[y][x] == 'X':
                print(colors.red+'X', end=colors.no)
            else:
                print(colors.yellow+'0', end=colors.no)
            print(colors.grey+'|', end=colors.no)
        print()

def check_fini():
    def check_columns():
        for ligne in grille:
            for x in range(3):
                if ligne[x] == ligne[x+1] == ligne[x+2] == ligne[x+3] != None:
                    return ligne[x]
    def check_ligne():
        for x in range(4):
            for y in range(6):
                if grille[x][y] == grille[x+1][y] == grille[x+2][y] == grille[x+3][y] != None:
                    return grille[x][y]

    def check_diago1():
        for y in range(-3, 0):
            for x in range(4):
                if (grille[x][y]==grille[x+1][y-1]==grille[x+2][y-2]==grille[x+3][y-3]!=None):
                    return grille[x][y]
    
    def check_diago2():
        for y in range(-3, 0):
            for x in range(3, 7):
                if (grille[x][y]==grille[x-1][y-1]==grille[x-2][y-2]==grille[x-3][y-3]!=None):
                    return grille[x][y]

    
    
    r=None
    r = check_columns()
    if not r: r = check_ligne()
    if not r: r = check_diago1()
    if not r: r = check_diago2()
    
    return r

def play(joueur:int) -> int:
    clear()
    print_grille()
    coup = int(input(f'Joueur {joueur}, à toi !! '))
    while grille[coup-1][0] != None or not (1<=coup<=7):
        coup = int(input('La columne est déjà pleine, réessaie !! '))
    place_jeton(coup, joueur)

def manual_play():
    end=None
    while not end:
        play(1)
        end=check_fini()
        if end:break

        play(2)
        end=check_fini()

        if not None in [grille[x][0] for x in range(grille)]:
            end=True


    print_grille()
    if end!=True:
        print('Le joueur', end, 'a gagné !!')
    else:
        print('Ex-Eaco !!!')

def debug_mode_player(coups1:list, coups2:list=[]):
    clear()
    for coup in coups1:
        place_jeton(coup, 1)
    for coup in coups2:
        place_jeton(coup, 2)
    print_grille()
    print('Le joueur', check_fini(), 'a gagné !! (DEBUG MODE)')
    
exit()
def autoplay():
    def auto_play(joueur:int) -> int:
        print_grille()
        coup = randint(1, 7)
        while grille[coup-1][0] != None or not (1<=coup<=7):
            coup = randint(1, 7)
        place_jeton(coup, joueur)
        print()
    
    end=None
    while not end:
        auto_play(1)
        end=check_fini()
        if end:break

        auto_play(2)
        end=check_fini()

        if not None in [grille[x][0] for x in range(len(grille))]:
            end=True


    print_grille()
    if end!=True:
        print('Le joueur', end, 'a gagné !! (DEBUG MODE)')
    else:
        print('Ex-Eaco !!! (DEBUG MODE)')
        for a in grille:
            print(a)

autoplay()
while not input('CONTINUE ? ').lower() == 'n':
    reset_grille()
    autoplay()

