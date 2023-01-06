def ex3(age: int) -> int:
    money = 0

    for annee in range(age+1):
        money+=100+annee*2
    
    return money

def ex4(lst: list, n: int) -> bool:
    for elt in lst:
        if elt == n:
            return True
    
    return False

def ex5() -> None:
    citation = 'Je ne cherche pas à connaître les réponses, je cherche à comprendre les questions'
    compteur = 0

    for elt in citation:
        if elt == 'i':
            compteur = compteur+1
    print(compteur)

def ex8(n: int) -> int:
    assert n>0, "n doit être plus grand que 0"

    S = 0
    i = 0
    while i < n:
        S+=i if i%2 == 1 else 0
        i+=1        
    return S

def ex9(moy: int) -> int:
    assert moy > 0, 'Le nombre moyen doit être plus grand que 0'
    return 13500//moy+1 if 13500%moy != 0 else 13500//moy

def ex10(lst: list, n: int) -> bool:
    i = -1
    while i < len(lst)-1:
        i+=1
        if lst[i] == n:
            return True
    return False

def ex11a() -> None:
    from random import randint
    secret_nbe = randint(0, 100)
    nbe = int(input('Donnez un entier entre 0 et 100 ? '))
    if nbe == secret_nbe:
        print("Bravo ! Vous avez gagnés !")
    
    while nbe != secret_nbe:
        if nbe > secret_nbe:
            nbe = int(input("La réponse est inférieure à votre proposition. Essayez encore ! "))
        else:
            nbe = int(input("La réponse est supérieure à votre proposition. Essayez encore ! "))
        
        if nbe == secret_nbe:
            print("Bravo ! Vous avez gagnés !")

def ex11b(nbe_coups_max: int) -> None:
    assert type(nbe_coups_max) == int, 'Le nombre de coups doit être un entier.'
    assert nbe_coups_max > 0, 'Le nombre de coups doit être supérieur à 0.'
    from random import randint
    secret_nbe = randint(0, 100)
    nbe_coups = 1
    nbe = int(input('1. Donnez un entier entre 0 et 100 ? '))
    if nbe == secret_nbe:
        print("Bravo ! Vous avez gagnés !")
    
    while nbe != secret_nbe and nbe_coups_max > nbe_coups:
        nbe_coups+=1
        if nbe > secret_nbe:
            nbe = int(input(str(nbe_coups)+". La réponse est inférieure à votre proposition. Essayez encore ! "))
        else:
            nbe = int(input(str(nbe_coups)+". La réponse est supérieure à votre proposition. Essayez encore ! "))
        
        if nbe == secret_nbe:
            print("Bravo ! Vous avez gagnés en", str(nbe_coups), 'coups !!!')
            return
    
    print('Oooooooh, vous avez perdu en', nbe_coups_max, 'coups... Dommage... le nombre secret était', secret_nbe)

def ex12() -> int:
    fric = 500
    annees = 0
    while fric<700:
        annees+=1
        fric*=1.01
    return annees

def ex13() -> bool:
    value = -1
    for x in range(10):
        value = float(input('Veuillez rentrer un nombre positif: '))
        if value > 0:
            return True
    
    print("Trop d'échecs ont étés détectés.")
    return False
        
def ex14a() -> int:
    liste_notes = list()

    def continuer() -> bool:
        return False if input('Voulez vous continuer').upper() == 'NON' else True
    def moyenne(liste_notes):
        somme = 0
        for element in liste_notes:
            somme+=element
        return somme/len(liste_notes)
    
    while continuer():
        liste_notes.append(float(input('Quel est la nouvelle note ? ')))
    
    return moyenne(liste_notes)

def ex14b(moy: float, nbe_notes: int, new_note: float):
    moy = (moy*nbe_notes+new_note)/(nbe_notes+1)
    return moy
    pass

def ex14c():
    def continuer() -> bool:
        return False if input('Voulez vous continuer ? ').upper() == 'NON' else True
    def moyenne(moy: float, nbe_notes: int, new_note: float):
        moy = (moy*nbe_notes+new_note)/(nbe_notes+1)
        return moy
    
    moy = 0
    nbe_notes = 0

    while continuer():
        moy = moyenne(moy, nbe_notes, float(input('Quel est la nouvelle note ? ')))
        nbe_notes+=1
    
    return moy

def ex15():
    from random import randint
    def somme(lst):
        n = 0
        for element in lst:
            n+=element
        return n
    def remplir_sac():
        lst = list()
        while somme(lst) < 20000:
            lst.append(randint(10, 500))
        
        return lst
    def moyenne(lst):
        return somme(lst)/len(lst)
    
    return moyenne(remplir_sac())

def ex16(n):
    from random import choice
    from os import system
    system('')
    def find_color():
        return choice(("\u001b[31m", "\u001b[32m", "\u001b[33m", "\u001b[34m", "\u001b[35m", "\u001b[96m", "\u001b[37m", "\u001b[0m")) 
    def star():
        for x in range(round(n/10)+1):
            f = n-x-1
            print("\u001b[33m", end='')
            for k in range(f+1):
                print(' ', end='')
            for k in range(x):
                print('*', end='')
            for k in range(x-1):
                print('*', end='')
            print()
        
    
    n+=1
    for x in range(1, n):
        f = n-x-1
        for k in range(f+1):
            print("\u001b[30m", end='')
            print(' ', end='')
        for k in range(x):
            print(find_color(), end='')
            print('*', end='')
        for k in range(x-1):
            print(find_color(), end='')
            print('*', end='')
        for k in range(f+1):
            print("\u001b[30m", end='')
            print(' ', end='')
        print()
    

ex16(5)