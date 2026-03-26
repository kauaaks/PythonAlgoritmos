def maior_menor(qtd):
    maior = 0
    menor = None
    for _ in range(qtd):
        n = float(input("Número positivo: "))
        if n > maior:
            maior = n
        if menor is None or n < menor:
            menor = n
    print("Maior:", maior)
    print("Menor:", menor)

maior_menor(100)