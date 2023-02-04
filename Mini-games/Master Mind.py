from random import choice
from os import system
system('')
class real_colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    violet = '\033[95m'
    cyan = '\033[96m'
    grey = '\033[90m'

    no = '\033[0m'
    gras = '\033[1m'
    souligné = '\033[4m'

    def random_color():
        return choice([real_colors.yellow, real_colors.violet, real_colors.red, real_colors.blue, real_colors.cyan, real_colors.green, real_colors.no])

def get_secret_key(nbe_fois: int = 4) -> list:
    return [choice(['A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']) for e in range(nbe_fois)]

def get_nbe_appair(key, liste):
    n = 0
    for l in liste:
        if key == l:
            n+=1
    return n

def clear_console():
    system('cls')

def print_regles(nbe_caracteres):
    text = f"""Ce jeu de Master mind a été créé par {real_colors.blue}Ezéchiel{real_colors.no} pendant les cours de NSI. Il a pour but de divertir, mais n'est en aucun cas responsable de mauvaises notes.
Les règles du jeu sont très simple. Le but est de deviner une combinaison de lettres générées aléatoirement par l'ordinateur.
Pour ce faire, l'utilisateur va devoir rentrer une combinaison de {nbe_caracteres} caractères (nombre modifiable en début de partie).
Ils doivent être compris entre: A, Z, E, R, T, Y, U, I, O, P, soit la première ligne de caractères du clavier français. 

Chaque charactère entré sera scanné et des couleurs vont s'afficher dans la console.
{real_colors.green}vert{real_colors.no} signifie que la lettre est bien placée.
{real_colors.yellow}jaune{real_colors.no} signifie que la lettre est présente mais mal placée.
{real_colors.grey}gris{real_colors.no} signifie que la lettre n'est pas présente dans la chaîne secrète.

Si toutes les lettres sont {real_colors.green}vertes{real_colors.no}, alors le jeu est terminé et vous pouvez recommencer une partie.
"""
    print(text)

print_regles(5)
nbe_caracteres = ''
while type(nbe_caracteres) != int:
    try:
        nbe_caracteres = int(input('Nombre de caractères ? '))
    except:
        pass
secret_key = get_secret_key(nbe_caracteres)
user_values = list()
user_history = list()
while not secret_key == user_values:
    user_values = list(input(f'Liste de charactères numéro {len(user_history)+1} ? ').upper())

    if user_values == ['C', 'L', 'S']: break
    elif len(user_values) != len(secret_key): continue

    list_reps = list()
    found = list()
    n = 0

    for lettre in user_values:
        if lettre == secret_key[n]:
            list_reps.append(True)
            found.append(lettre)
        else:
            list_reps.append(None)
        n+=1
    n = -1
    for lettre in user_values:
        n+=1
        if list_reps[n] == True:
            continue
        nbe_lettre = get_nbe_appair(lettre, secret_key)
        nbe_lettre2 = get_nbe_appair(lettre, found)

        if nbe_lettre > nbe_lettre2:
            list_reps[n] = False
            found.append(lettre)
    clear_console()
    n = 0
    t = str(real_colors.gras)
    for e in list_reps:
        if e:
            t+=real_colors.green + user_values[n]
        elif e == False:
            t+=real_colors.yellow + user_values[n]
        else:
            t+=real_colors.grey + user_values[n]
        n+=1
    user_history.append(t)
    print('\n'.join(user_history))
    print(real_colors.no)
print(real_colors.green+f'Bravo, tu as gagné en {len(user_history)} coups !!! Dépeche toi de refaire une partie pour battre ton score ;)', real_colors.no)