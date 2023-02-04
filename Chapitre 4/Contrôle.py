def occurrence_dans_liste(lst: list, n: int) -> int:
    "Retourne le nombre d'occurrence d'un entier dans une liste"
    
    nbe_fois = 0
    for nbe in lst:
        if nbe == n:
            nbe_fois+=1
    
    return nbe_fois

def cout_puits(n: int) -> int:
    "retourne le prix pour creuser un trou de n mètres de profondeur"

    assert n > 0, 'Le nombre de mètres doit être supérieur à 0'
    prix = 800
    for x in range(n):
        prix+=50+(5*x)#CALCULE LE PRIX DU METRE ET L'AJOUTE AU PRIX FINAL
    return prix

def attendre(objectif: float) -> int:
    argent = 1200
    assert type(objectif) == int and objectif>argent, "L'objectif doit être un entier supérieur au capital de base."
    nbe_années = 0

    while argent < objectif:
        nbe_années+=1
        argent+=(1.3/100)*argent
    
    assert nbe_années < 100, "Le nombre d'années est trop grand, vous serez déjà mort !!"
    return nbe_années

