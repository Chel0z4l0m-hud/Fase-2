def es_par(n):
    if n == 0:
        return True
    return es_impar(n - 1)

def es_impar(n):
    if n == 0:
        return False
    return es_par(n - 1)

print(es_impar(7)) 
print(es_impar(4))   