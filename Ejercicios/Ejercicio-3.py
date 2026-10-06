def insercion_orden(lista, indice=1):
    if indice >= len(lista):
        return lista
    valor = lista[indice]
    j = indice
    while j > 0 and lista[j - 1] > valor:
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = valor
    return insercion_orden(lista, indice + 1)

print(insercion_orden([5, 2, 8, 1, 3]))  