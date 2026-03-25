def exercicio20():
    import math
    A = float(input("Digite A: "))
    B = float(input("Digite B: "))
    C = float(input("Digite C: "))
    delta = B**2 - 4*A*C
    if delta < 0:
        print("Não existem raízes reais.")
    else:
        x1 = (-B + math.sqrt(delta)) / (2*A)
        x2 = (-B - math.sqrt(delta)) / (2*A)
        print("x1 =", x1)
        print("x2 =", x2)

exercicio20()