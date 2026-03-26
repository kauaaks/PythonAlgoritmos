def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    print(fat)

num = int(input("Número: "))
fatorial(num)