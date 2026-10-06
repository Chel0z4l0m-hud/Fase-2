def menor_vector(vector, indice=0):
    if indice == len(vector) - 1:
        return vector[indice]
    minimo_resto = menor_vector(vector, indice + 1)
    if vector[indice] < minimo_resto:
        return vector[indice]
    return minimo_resto

print(menor_vector([5, 3, 8, 1, 9]))  