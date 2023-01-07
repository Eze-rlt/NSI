def ex1() -> str:
    return "5x1000 + 6x100 + 2x10 + 4x1\n5x10³ + 6x10² + 2x10¹ + 4x10⁰"

def decimal_to_binaire(nbe: int) -> int:
    assert type(nbe) == int and nbe>=0, "Le nombre doit être un entier supérieur ou égal à 0"

    p = q = 0
    while nbe>0:
        p+=(nbe%2)*10**q
        q+=1
        nbe//=2
    
    return p

def binaire_to_decimal(nbe: int) -> int:
    assert type(nbe) == int and nbe>=0, "Le nombre doit être un entier supérieur ou égal à 0"
    nbe = str(nbe)
    n2 = int()
    p = 0
    for n in nbe[::-1]:
        n2+=int(n)*2**p
        p+=1
    return n2

def binaire_to_decimal2(nbe: int) -> int:
    assert type(nbe) == int and nbe>=0, "Le nombre doit être un entier supérieur ou égal à 0"
    
    nbe = [int(k) for k in str(nbe)][::-1]
    n = 0
    p = 1
    for x in range(len(nbe)):
        n += nbe[x]*p
        p*=2
    return n

    


nbe = 58
b = decimal_to_binaire(nbe)
d = binaire_to_decimal2(b)

print(b, d)