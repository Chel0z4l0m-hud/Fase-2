import time

def fib_recursivo(n):
    if n == 0 or n == 1:
        return n
    return fib_recursivo(n - 1) + fib_recursivo(n - 2)

def fib_iterativo(n):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 30

inicio = time.time()
print("Recursivo:", fib_recursivo(n), "-", time.time() - inicio)

inicio = time.time()
print("Iterativo:", fib_iterativo(n), "-", time.time() - inicio)