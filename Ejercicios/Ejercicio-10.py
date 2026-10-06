def formas_robot(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return formas_robot(n - 1) + formas_robot(n - 2)

print(formas_robot(5))  