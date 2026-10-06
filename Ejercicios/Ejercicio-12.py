def potencia(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        mitad = potencia(base, exp // 2)
        return mitad * mitad
    else:
        mitad = potencia(base, (exp - 1) // 2)
        return mitad * mitad * base

print(potencia(2, 10))  