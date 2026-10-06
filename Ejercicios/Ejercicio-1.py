def maximo_lista(lista, indice=0):
    if indice == len(lista) - 1:
        return lista[indice]
    maximo_resto = maximo_lista(lista, indice + 1)
    if lista[indice] > maximo_resto:
        return lista[indice]
    return maximo_resto

print(maximo_lista([3, 7, 2, 9, 4]))  