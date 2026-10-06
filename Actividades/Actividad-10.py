def suma_matriz(matriz, fila=0, col=0):
    if fila == len(matriz):
        return 0
    if col == len(matriz[fila]):
        return suma_matriz(matriz, fila + 1, 0)
    return matriz[fila][col] + suma_matriz(matriz, fila, col + 1)

m = [[1, 2], [3, 4], [5, 6]]
print(suma_matriz(m)) 