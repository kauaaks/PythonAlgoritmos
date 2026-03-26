def serie():
    soma = 1
    num = 2
    den = 3
    for _ in range(49):
        soma += num/den
        num += 1
        den += 2
    print(soma)

serie()