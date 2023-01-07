def ex1() -> str:
    return "5x1000 + 6x100 + 2x10 + 4x1\n5x10³ + 6x10² + 2x10¹ + 4x10⁰"

def base(nbe: int, base_src: int = 10, base_dest: int = 2) -> int:
    assert type(nbe) == int and nbe>=0, "Le nombre à convertir doit être un entier supérieur ou égal à 0"
    assert type(base_src) == int and base_src>0, "La base de source doit être un entier supérieur à 0"
    assert type(base_dest) == int and base_dest>0, "La base de destination doit être un entier supérieur à 0"
    assert base_src >= max([int(v) for v in str(nbe)]), "Le rapport entre la base et le nombre n'est pas correct. Veuillez réessayer."
    
    new_nbe = nbe_loop = 0
    while nbe>0:
        new_nbe+=(nbe%base_dest)*base_src**nbe_loop
        nbe_loop+=1
        nbe//=base_dest
    
    return new_nbe

print(base(255))