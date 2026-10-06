def suma_vector(vector, indice=0):
    if indice == len(vector):
        return 0
    return vector[indice] + suma_vector(vector, indice + 1)

print(suma_vector([1, 2, 3, 4, 5]))  