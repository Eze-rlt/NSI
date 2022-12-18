def etat_eau(tempe: int) -> str:
    """
    Fonction qui dit l'etat de l'eau à la temperature tempe donnée
    """

    assert type(tempe) == int, "Tempe doit être un entier int"
    assert tempe >= -273, "Tempe doit être supérieure à -273"

    if tempe < 0: return "solide"
    elif tempe > 100: return "gazeux"
    elif 0 <= tempe <= 100: return "liquide"


def table_multi(nbe: int) -> str():
    for x in range(10+1):
        print(f'{x} fois {nbe} = {x*nbe}')

table_multi(5)
