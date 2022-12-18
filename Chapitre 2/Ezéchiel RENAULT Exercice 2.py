#Programme de Ezéchiel Renault, 1è8, Exercice 2
from math import sqrt
def temps(p: float) -> float:
    """
    Ce programme renvoie la valeur du temps d'attente avant que la pierre ne touche le fond du puit.
    """
    assert type(p) in (int, float), "La profondeur doit être de type float ou int"
    assert p >= 0, "La profondeur doit être supérieur ou égale à 0"

    t = float(sqrt(p/4.9)+(p/330))

    assert type(t) == float, "Le résultat n'est pas un flotant (float), désolé"

    return t
