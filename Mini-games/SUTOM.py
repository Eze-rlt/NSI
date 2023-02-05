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
        hell_grey = "\033["
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
        double_underline = "\033[21m"
        strikethrough = "\033[9m" 
        italics = "\033[3m"
        reset = "\033[0m"
    def colorize(font: str='no',
                highlight: str='no',
                bold:bool=False,
                underline:bool=False,
                double_underline:bool=False,
                strikethrough:bool=False,
                italics:bool=False):
        if not highlight in list(colors.highlight.__dict__.keys())[1:-3]:
            print('HIGHLIGHT NOT GOOD')
            return
        elif not font in list(colors.font.__dict__.keys())[1:-3]:
            print('FONT NOT GOOD')
            return

        print(colors.font.__dict__[font]+colors.highlight.__dict__[highlight], end='')

        if bold: print(colors.specific.bold, end='')
        if underline: print(colors.specific.underline, end='')
        if double_underline: print(colors.specific.double_underline, end='')
        if strikethrough: print(colors.specific.strikethrough, end='')
        if italics: print(colors.specific.italics, end='')
    def reset():
        print(colors.specific.reset, end='')

def get_nbe_appair(word: str, lettre: str) -> int:
    n = 0
    
    for l in word:
        if l == lettre:
            n+=1
    return n

def compare_words(secret_word: str, user_word: str) -> list:
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
            resultat[n] = False
            found.append(lettre)

    return resultat

user_word = ''
colors.reset()
while not user_word.lower() == secret_word.lower():
    user_word = input('Word ? ')
    if len(user_word) != len(secret_word):
        continue
    result = compare_words(secret_word, user_word)
    for l in range(len(user_word)):
        if result[l]:
            colors.colorize(font='white', highlight='green', bold=True)
        elif result[l] is False:
            colors.colorize(font='white', highlight='yellow', bold=True)
        else:
            colors.colorize(font='white', highlight='red', bold=True)
        print(user_word[l].capitalize(), end='')
        colors.reset()
    print()