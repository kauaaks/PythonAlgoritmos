def potencia(base, exp):
    resultado = 1
    for _ in range(exp):
        resultado *= base
    print(resultado)

b = int(input("Base: "))
e = int(input("Expoente: "))
potencia(b, e)