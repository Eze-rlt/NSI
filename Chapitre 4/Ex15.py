from random import randint
def somme(lst):
    n = 0
    for element in lst:
        n+=element
    return n
    
def remplir_sac():
    lst = list()
    while somme(lst) < 20000:
        lst.append(randint(10, 500))
    
    return lst
def moyenne(lst):
    return somme(lst)/len(lst)
