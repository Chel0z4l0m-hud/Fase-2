import random

def desordena(a, n):
    if n <= 1:
        return a
    
    indice_aleatorio = random.randint(0, n - 1)
    a[n - 1], a[indice_aleatorio] = a[indice_aleatorio], a[n - 1]
    
    return desordena(a, n - 1)

lista = [1, 2, 3, 4, 5]
print(f"Lista original: {lista}")
print(f"Lista desordenada: {desordena(lista.copy(), len(lista))}")