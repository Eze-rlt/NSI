#Programme de Ezéchiel Renault, 1è8, Exercice 1
def Somme(n: int) -> int:
    """
    renvoie la somme des entiers de 0 au nombre donné.
    """
    assert type(n)==int, "N doit être un entier."
    assert n>0, "N doit être positif et non-n."

    total = int()
    for x in range(n+1):
        total+=x
    
    assert type(total)==int, "Le résultat trouvé n'est pas un entier, désolé…"
    return total
