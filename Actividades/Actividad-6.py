def multiplicar_vector(vector, indice=0):
    if indice == len(vector):
        return 1
    return vector[indice] * multiplicar_vector(vector, indice + 1)

print(multiplicar_vector([2, 3, 4])) 