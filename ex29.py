def exercicio29(tipo, valor):
    if tipo == 1:
        valor_corrigido = valor * 1.03
        print("Valor corrigido:", valor_corrigido)
    elif tipo == 2:
        valor_corrigido = valor * 1.05
        print("Valor corrigido:", valor_corrigido)
    else:
        print("Tipo de investimento inválido.")

t = int(input("Tipo de investimento (1=poupança, 2=renda fixa): "))
v = float(input("Valor do investimento: "))

exercicio29(t, v)