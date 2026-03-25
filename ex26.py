def exercicio26():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    maior = max(a, b)
    menor = min(a, b)
    if maior % menor == 0:
        print("O maior é múltiplo do menor.")
    else:
        print("O maior NÃO é múltiplo do menor.")

exercicio26()