def seleccion_orden(lista, indice=0):
    if indice >= len(lista) - 1:
        return lista
    min_idx = indice
    for i in range(indice + 1, len(lista)):
        if lista[i] < lista[min_idx]:
            min_idx = i
    lista[indice], lista[min_idx] = lista[min_idx], lista[indice]
    return seleccion_orden(lista, indice + 1)

print(seleccion_orden([5, 2, 8, 1, 3]))  