def ex1() -> str:
    return "5x1000 + 6x100 + 2x10 + 4x1\n5x10³ + 6x10² + 2x10¹ + 4x10⁰"

def base(nbe: int, base_src: int = 10, base_dest: int = 2) -> int:
    assert type(nbe) == int and nbe>=0, "Le nombre à convertir doit être un entier supérieur ou égal à 0"
    assert type(base_src) == int and base_src>0, "La source de base doit être un entier supérieur à 0"
    assert type(base_dest) == int and base_dest>0, "La destination de base doit être un entier supérieur à 0"
    p = q = 0
    while nbe>0:
        p+=(nbe%base_dest)*base_src**q
        q+=1
        nbe//=base_dest
    
    return p


nbe = 39
print(base(nbe, 2, 10))