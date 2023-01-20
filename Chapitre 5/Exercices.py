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

def base2(nbe: str(), base_src=16, base_dest=10):
    chars = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    nbes = [chars.index(char) for char in str(nbe)][::-1]
    
    new_nbe = nbe_loop = 0
    for nbe in nbes:
        new_nbe+=nbe*base_src**nbe_loop
        nbe_loop+=1
    if base_dest < 10:
        new_nbe = base(new_nbe, 10, base_dest)
    return new_nbe

print(base2('4F3B', 16, 2))
print(base2('100111100111011', 2, 16))