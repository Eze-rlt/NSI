import random

def tableau_aleatoire(n:int, a:int, b:int) -> list:
    tab = list()
    for x in range(n):
        aléatoire = random.randint(a, b)
        tab.append(aléatoire)
    return tab

def melange(tab:list) -> list:
    taille_tab = len(tab)
    for i in range(taille_tab):
        j = random.randint(0, i)
        valeur1 = tab[i]
        valeur2 = tab[j]
        tab[i] = valeur2
        tab[j] = valeur1
    return tab

def est_reçu(liste_prenoms:tuple, utilisateur:str) -> bool:
    reçu = False
    for n in liste_prenoms:
        if utilisateur==n:
            reçu = True
    return reçu

def trouver(lst:list, val:int)->list:
    places = list()
    taille_liste = len(lst)

    for x in range(0, taille_liste):
        if lst[x]==val:
            places.append(x)
    return places

L = [1, 2, 3, [4]]
M = [0, 0, 0, 0]

for i in range(len(L)):
    M[i] = L[i]
    M[1] = 10
print(L)