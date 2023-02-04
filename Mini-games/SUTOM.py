from random import choice
words = ['panda', 'colie', 'prier', 'parle', 'pisse']
secret_word = choice(words)

class colors:
    class highlight:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        yellow = "\033[43m"
        blue = "\033[44m"
        purple = "\033[45m"
        cyan = "\033[46m"
        white = "\033[47m"
        no = "\033[4m"
    
    class font:
        gray = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
        white = "\033[37m"
        no = "\033[4m"
    
    class specific:
        bold="\033[1m"
        underline = "\033[4m"
        italics = "\033[3m"
        reset = "\033[0m"
        
        
    for x in range(100):
        break
        print(f"\033[{x}m {x} ", end='')


def get_nbe_appair(word: str, lettre: str) -> int:
    n = 0
    
    for l in word:
        if l == lettre:
            n+=1
    return n


def compare_words(secret_word: str, user_word: str) -> list:
    print(list(user_word))
    found = list()
    resultat = list()
    n = int()
    for lettre in secret_word:
        if lettre == user_word[n]:
            resultat.append(True)
            found.append(lettre)
        else:
            resultat.append(None)
        n+=1
    
    n = -1
    for lettre in user_word:
        n+=1
        
        if resultat[n]:
            continue

        nbe_lettre_secret = get_nbe_appair(secret_word, lettre)
        nbe_lettre_user = get_nbe_appair(found, lettre)

        if nbe_lettre_secret > nbe_lettre_user:
            print(lettre, nbe_lettre_secret, nbe_lettre_user, n)
            resultat[n] = False
            found.append(lettre)

        
        


    return resultat

user_word = 'paad'
secret_word = 'panda'
result = compare_words(secret_word, user_word)
for l in range(len(user_word)):
    if result[l]:
        print(colors.green)