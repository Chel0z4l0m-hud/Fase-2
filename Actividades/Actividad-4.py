def mult_rusa(a, b):
    if a == 0 or b == 0:
        return 0
    if b % 2 == 0:
        return mult_rusa(a * 2, b // 2)
    return a + mult_rusa(a * 2, b // 2)

print(mult_rusa(12, 12))  