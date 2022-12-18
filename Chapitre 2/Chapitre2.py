def exercice1():
    #PETIT 1
    a = 5
    print('id de a:', str(id(a)))

    #PETIT 3
    b = a
    print('id de b:', str(id(b)))


    
    #PETIT C
    b = "mot"
    print('nouvel id de b:', str(id(b)))

def exercice2():
    print("Mots", "et", "valeur", 3.141159, "à afficher", sep='\n')

class exercice5:
    def convertir(durée_minutes: int) ->tuple:
        """
        fonction qui calcule le noombre de minutes grâce à la division œclidienne"""
        return (durée_minutes//60, durée_minutes%60)

def exercice10() -> float:
    """
    """
    masse = int(input('Masse en kg ? '))#80
    taille = int(input('Taille en cm ? '))#180

    taille = taille/100

    return masse/(taille**2)

class exercice11:
    def dire_bonjour(mot:str()) -> str:
        assert len(mot) >= 3, "Entrez un nom d'utilisateur plus grand"
        return print('Bonjour', mot, '!')

class exercice15:
    def cherche_lettre(nom: str, lettre: str):
        assert type(nom) == str
        assert type(lettre) == str
        assert len(lettre) == 1
        assert lettre != ''

        if lettre in nom:
            print(lettre, 'est dans le nom', nom)
        else:
            print(lettre, "n'est pas dans le nom", nom)
    
        return

def exercice16(liste: list) -> int:
    maximum = liste[0]
    for nbe in liste:
        if nbe>maximum:
            maximum = nbe
    
    return maximum

class exercice17:
    def div_euclidienne(a:int, b:int)->tuple:
        assert type(a) == type(b) == int, "entrez des int"
        assert b!=0, "Hey, on peut pas diviser par 0 !!"
        i = a//b
        a = a%b

        assert type(a) == type(i) == int, "Aïe, les variables retournées ne sont pas des entiers"

        return (a, i)

class exercice18:
    def get_max_position(liste:list) -> tuple:
        maximum = liste[0]
        place = 0
        for nbe in liste:
            if nbe>maximum:
                maximum = nbe
                place = liste.index(nbe)
        

        assert place == len(liste)-1, "la place n'est pas correcte"
        assert liste[place] == maximum, "la valeur du maximum n'est pas correcte"
        return (maximum, place)
