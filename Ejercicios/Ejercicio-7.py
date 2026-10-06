import time
import random

def insercion(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i
        while j > 0 and lista[j - 1] > valor:
            lista[j] = lista[j - 1]
            j -= 1
        lista[j] = valor
    return lista

def seleccion(lista):
    for i in range(len(lista) - 1):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

datos = [random.randint(1, 1000) for _ in range(1000)]

inicio = time.time()
insercion(datos.copy())
print("Inserción:", time.time() - inicio)

inicio = time.time()
seleccion(datos.copy())
print("Selección:", time.time() - inicio)