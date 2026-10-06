import time

def factorial_recursivo(n):
    if n == 0:
        return 1
    return n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = 100

inicio = time.time()
factorial_recursivo(n)
print("Recursivo:", time.time() - inicio)

inicio = time.time()
factorial_iterativo(n)
print("Iterativo:", time.time() - inicio)