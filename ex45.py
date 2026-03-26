def serie():
    soma = 0
    sinal = 1
    for i in range(1, 16):
        soma += sinal * (i / (i*i))
        sinal *= -1
    print(soma)

serie()