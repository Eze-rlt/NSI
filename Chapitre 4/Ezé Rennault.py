def ex9(moy: int) -> int:
    assert moy > 0, 'Le nombre moyen doit être plus grand que 0'
    return 13500//moy+1 if 13500%moy != 0 else 13500//moy

def ex11a() -> None:
    from random import randint
    secret_nbe = randint(0, 100)
    nbe = int(input('Donnez un entier entre 0 et 100 ? '))
    if nbe == secret_nbe:
        print("Bravo ! Vous avez gagnés !")
    
    while nbe != secret_nbe:
        if nbe > secret_nbe:
            nbe = int(input("La réponse est inférieure à votre proposition. Essayez encore ! "))
        else:
            nbe = int(input("La réponse est supérieure à votre proposition. Essayez encore ! "))
        
        if nbe == secret_nbe:
            print("Bravo ! Vous avez gagnés !")
