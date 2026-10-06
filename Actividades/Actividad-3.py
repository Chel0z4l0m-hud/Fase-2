def invertir(n, acum=0):
    if n == 0:
        return acum
    return invertir(n // 10, acum * 10 + n % 10)

print(invertir(6745))  