from os import system

class colors:
    yellow = '\33[93m'
    red = '\33[91m'
    grey = '\33[90m'
    no = '\33[0m'

grille = [[None for s in range(6)] for x in range(7)]

def clear():
    system('cls')

def place_grille(x: int, joueur: int):
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
        for x in range(3):
            for y in range(6):
                if grille[x][y] == grille[x+1][y] == grille[x+2][y] == grille[x+3][y] != None:
                    return grille[x][y]
    def check_diago1():#BAS-> HAUT ; GAUCHE -> DROITE
        for x in range(4):
            for y in range(3):
                if grille[x][y] == grille[x+1][y+1] == grille[x+2][y+2] == grille[x+3][y+3] != None:
                    #LES DIAGOS -> VERS HAUT ; GAUCHE -> DROITE
                    print(1)
                    return grille[x][y]
    def check_diago2():#BAS-> HAUT ; DROITE -> GAUCHE
        for x in range(3, 6):
            for y in range(3):
                if grille[x][y] == grille[x-1][y+1] == grille[x-2][y+2] == grille[x-3][y+3] != None:
                    #LES DIAGOS BAS VERS HAUT? GAUCHE VERS DROITE
                    print(2)
                    return grille[x][y]
    
    r=None
    r = check_ligne()
    r = check_columns() if not r else r
    r = check_diago1() if not r else r
    r = check_diago2() if not r else r
    if r: return r

end=None
clear()
while not end:
    print_grille()
    j1 = int(input('Joueur 1, à toi !! '))
    while grille[j1-1][0] != None or not (1<=j1<=7):
        j1 = int(input('La columne est déjà pleine, réessaie !! '))
    place_grille(j1, 1)
    end=check_fini()
    clear()

    
    if not end:
        print_grille()
        j2 = int(input('Joueur 2, à toi !! '))
        while grille[j2-1][0] != None or not (1<=j2<=7):
            j2 = int(input('La columne est déjà pleine, réessaie !! '))
        place_grille(j2, 2)
        end=check_fini()
        clear()

print_grille()
print('Le joueur', end, 'a gagné !!')