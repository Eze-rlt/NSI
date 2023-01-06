def ex1() -> str:
    return "5x1000 + 6x100 + 2x10 + 4x1\n5x10³ + 6x10² + 2x10¹ + 4x10⁰"

def ex2(nbe: str) -> int:
    n = str(nbe%2)
    while nbe//2 >= 1:
        nbe = nbe//2
        n = str(nbe%2)+n
    return int(n)

def ex3() -> str:
    return ex2(197), ex2(119), ex2(243)

print(ex3())