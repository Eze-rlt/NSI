def decbin(nbe: int) -> list:
    assert type(nbe) == int and nbe>=0, "Le nombre à convertir doit être un entier supérieur ou égal à 0"
    assert 10 >= max([int(v) for v in str(nbe)]), "Le rapport entre la base et le nombre n'est pas correct. Veuillez réessayer."
    
    new_nbe = nbe_loop = 0
    while nbe>0:
        new_nbe+=(nbe%2)*10**nbe_loop
        nbe_loop+=1
        nbe//=2
    return [int(n) for n in str(new_nbe)]

def deci_en_bin(nbe: float) -> list:
    decimal = int(str(nbe).split('.')[1])/10**len(str(nbe).split('.')[1])
    while decimal > 1:
        decimal/=10
    print(decimal)
    bin_entier = decbin(int(nbe))
    bin_decimal = list()

    while decimal%1!=0 and len(bin_decimal+bin_entier)!=100000000:
        decimal*=2
        bin_decimal.append(round(decimal//1))
        if decimal>=1:
            decimal-=1
        
    return bin_entier+['.']+bin_decimal




print(deci_en_bin(13.325))
