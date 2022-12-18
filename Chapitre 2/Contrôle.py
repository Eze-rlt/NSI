#Programme de Ezéchiel Renault, 1è8
from math import sqrt

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

def temps(p: float) -> float:
    """
    Ce programme renvoie la valeur du temps d'attente avant que la pierre ne touche le fond du puit.
    """

    assert type(p) in (int, float), "La profondeur doit être de type float ou int"
    assert p >= 0, "La profondeur doit être supérieur ou égale à 0"

    t = float(sqrt(p/4.9)+(p/330))

    assert type(t) == float, "Le résultat n'est pas un flotant (float), désolé"

    return t
