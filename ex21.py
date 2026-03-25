def exercicio21():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))
    media = (n1 + n2 + n3 + n4) / 4
    print("Média =", media)
    if media >= 6:
        print("APROVADO")
    elif media >= 3:
        print("EXAME")
    else:
        print("RETIDO")

exercicio21()