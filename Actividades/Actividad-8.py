def positivo_o_negativo(n):
    if n == 0:
        return "Es cero"
    if n == 1:
        return "Es positivo"
    if n == -1:
        return "Es negativo"
    if n > 0:
        return positivo_o_negativo(n - 1)
    return positivo_o_negativo(n + 1)

print(positivo_o_negativo(10))   
print(positivo_o_negativo(-5))  