phrase = "LOOL"
step=10

def code(phrase:str, step:int)->str:
    lettres = '''Àêîô:ûÉÈâ;'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.\\/?,*µù%]°=+}@à0^ç9_8`7è|-6(5[{#"34~é2&1²§) \nÇ'''
    phrase2 = str()
    for l in phrase:
        phrase2+=lettres[(lettres.index(l)+step)%len(lettres)]
    
    return phrase2



def decode(phrase:str, step:int):
    return code(phrase, -step)

a = code(phrase, step)
print(a)