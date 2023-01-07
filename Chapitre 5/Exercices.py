def ex1() -> str:
    return "5x1000 + 6x100 + 2x10 + 4x1\n5x10³ + 6x10² + 2x10¹ + 4x10⁰"

def decimal_to_binaire(nbe: int) -> int:
    assert type(nbe) == int and nbe>=0, "Le nombre doit être un entier supérieur à 0"

    p = q = 0
    while nbe>0:
        p+=(nbe%2)*10**q
        q+=1
        nbe//=2
    
    return p

nbe = 58
print(decimal_to_binaire(nbe))