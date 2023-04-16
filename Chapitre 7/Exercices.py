def ex1():
    tup=(1, 4, 5, 'moto', (12, 'nsi', 'génial'), 4.6)
    print(tup[3])
    print(tup[-1])
    print(tup[1:3])
    print(tup[4][1:])

def ex2():
    jours_1=('lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi')
    jours_2=('samedi', 'dimanche')

    print('1.', 'samedi' in jours_1)
    print('2.', len(jours_2))
    print('3.', jours_1==jours_2)
    print('4.', jours_1[1])
    print('5.', jours_1[1: 4])
    print('6.', jours_2.index('dimanche'))
    print('7.', jours_2.count('samedi'))
    semaine = jours_1+jours_2
    print('8.', semaine)

def estdans(nbe: any, tup: tuple[any]):
    return nbe in tup

def milieu(xA: float, xB: float, yA: float, yB: float) -> tuple:
    return (xA+xB)/2, (yA+yB)/2

def triangle_rect(nbe: int) -> tuple[tuple[int, int, int]]:
    tples = tuple()
    for x in range(2, nbe):
        for y in range(2, x):
            for z in range(2, y+1):
                if x**2 == y**2+z**2:
                    tples+=((x, y, z),)
    return tuple(tples)

def ex6_extension():
    liste=list()
    for x in range(1, 10001):
        liste.append(x)
    return liste
def ex6_compréhension():
    return [x for x in range(1, 10001)]

def ex7_extension():
    liste = list()
    for x in range(10000):
        if not x%2:
            liste.append(x)

    return liste
def ex7_compréhension():
    return [x for x in range(10000) if not x%2]

def test(a: list) -> list:
    return [x**2 for x in a if x>0], [x for x in a if a > 10]

def ex9():
    import random
    liste=[random.randint(1, 6) for i in range(1000)]

    return liste.count(1), liste.count(2), liste.count(3), liste.count(4), liste.count(5), liste.count(6)

def ex10(nbe, liste):
    n=int()
    for e in liste:
        if e==nbe:
            n+=1
    return n
