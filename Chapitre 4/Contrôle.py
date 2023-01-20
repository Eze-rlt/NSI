def occurrence_dans_liste(lst, n):
    nombre_de_fois = 0
    for nombre in lst:
        if nombre == n:
            nombre_de_fois = nombre_de_fois+1
    
    return nombre_de_fois

def cout_puits(n):
    prix_total = 800
    prix_mètre=50
    for x in range(n):
        prix_total = prix_total+prix_mètre
        prix_mètre = prix_mètre+5

    return prix_total

def attendre(objectif):
    money = 1200
    assert objectif>money, "L'objectif doit être un entier supérieur au capital de base."
    nombre_années = 0

    while money < objectif:
        nombre_années = nombre_années+1
        money = money+(1.3/100)*money
    
    assert nombre_années <= 100, "Le nombre d'années est plus grand que 0"
    return nombre_années


print(attendre(1300))