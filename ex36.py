def serie_fatorial(n):
    soma = 0
    fat = 1
    for i in range(1, n + 1):
        fat *= i
        soma += 1/fat
    print(1 + soma)

num = int(input("N: "))
serie_fatorial(num)