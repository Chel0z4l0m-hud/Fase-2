def formas_robot_3(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return formas_robot_3(n - 1) + formas_robot_3(n - 2) + formas_robot_3(n - 3)

print(formas_robot_3(5))  #