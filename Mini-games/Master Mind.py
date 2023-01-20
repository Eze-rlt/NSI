from random import choice

class colors:
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    red = '\033[91m'
    violet = '\033[95m'
    yellow = '\033[93m'

    no = '\033[0m'
    gras = '\033[1m'
    souligné = '\033[4m'

    def random_color():
        return choice([colors.yellow, colors.violet, colors.red, colors.blue, colors.cyan, colors.green, colors.no])
def secret():
    return [choice(['b', 'c', 'g', 'r', 'v', 'y']) for n in range(6)]

secret_value = secret()
print(secret_value)
while True:
    secret_value2 = secret_value.copy()
    q = input('Quelles sont les couleurs ? ')
    rep = list()
    n = 0
    for e in list(q):
        print(n)
        if e == secret_value2[n]:
            secret_value2.pop(n)
            secret_value.insert(n, None)
            rep.insert(n, e)
        else:
            rep.insert(n, None)
        
        n+=1
    
    print(rep)

        

