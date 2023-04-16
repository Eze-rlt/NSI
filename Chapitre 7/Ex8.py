def test(a: list) -> list:
    return [x**2 for x in a if x>0], [x for x in a if a > 10]
