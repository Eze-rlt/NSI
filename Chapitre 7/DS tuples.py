from random import randint

def tableau_aleatoire(n:int, a:int, b:int) -> list:
    "Génère un tableau de longueur n remplies de nombres entiers aléatoires entre a et b"
    tableau = list()
    for x in range(n):
        tableau.append(randint(a, b))
    return tableau

def melange(tab:list) -> list:
    "Mélange le tableau tab grâce à l'algorithme du mélange de Knuth"
    for index1 in range(1, len(tab)):
        index2 = randint(0, index1)
        tab[index1], tab[index2] = tab[index2], tab[index1]
    return tab

def est_reçu(personnes:tuple, nom:str) -> bool:
    "Retourne True si le contenu de la variable nom est contenu dans le tuple personnes, sinon False"
    personnes = [personne.lower() for personne in personnes]
    return True if nom.lower() in personnes else False

def trouver(lst:list, val:int)->list:
    "Retourne tous les indexs de la variable val dans la liste lst."
    indexs = list()
    for e in range(len(lst)):
        if lst[e]==val:
            indexs.append(e)
    return indexs
