def primos(a, b):
    if a > b:
        a, b = b, a
    for n in range(a, b + 1):
        if n > 1:
            cont = 0
            for i in range(1, n + 1):
                if n % i == 0:
                    cont += 1
            if cont == 2:
                print(n)

x = int(input("A: "))
y = int(input("B: "))
primos(x, y)