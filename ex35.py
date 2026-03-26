def impares(a, b):
    if a > b:
        a, b = b, a
    soma = 0
    for i in range(a, b + 1):
        if i % 2 != 0:
            soma += i
    print("Maior:", b)
    print("Soma ímpares:", soma)

x = int(input("A: "))
y = int(input("B: "))
impares(x, y)