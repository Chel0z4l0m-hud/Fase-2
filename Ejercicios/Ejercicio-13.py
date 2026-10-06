def suma(a, b):
    if b == 0:
        return a
    return suma(a + 1, b - 1)

print(suma(5, 3)) 
