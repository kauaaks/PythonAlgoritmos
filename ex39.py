def graos():
    total = 0
    q = 1
    for _ in range(64):
        total += q
        q *= 2
    print(total)

graos()