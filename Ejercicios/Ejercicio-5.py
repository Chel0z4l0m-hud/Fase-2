import random

def desordena(a, n):
    if n <= 1:
        return a
    indice_aleatorio = random.randint(0, n - 1)
    a[n - 1], a[indice_aleatorio] = a[indice_aleatorio], a[n - 1]
    return desordena(a, n - 1)

lista_original = [1, 2, 3, 4, 5]
resultados = []

print("Ejecutando 'desordena' 10 veces con la misma entrada:\n")
for i in range(10):
    resultado = desordena(lista_original.copy(), len(lista_original))
    resultados.append(tuple(resultado))
    print(f"Ejecución {i+1}: {resultado}")

unicos = set(resultados)
print(f"\nResultados únicos obtenidos: {len(unicos)} de 10 ejecuciones")

if len(unicos) > 1:
    print("El algoritmo es impredecible (produce diferentes salidas)")
else:
    print("El algoritmo NO es impredecible (siempre da el mismo resultado)")