def buscar_texto(lista, texto, indice=0):
    if indice == len(lista):
        return False
    if lista[indice] == texto:
        return True
    return buscar_texto(lista, texto, indice + 1)

print(buscar_texto(["hola", "mundo", "python"], "mundo"))  