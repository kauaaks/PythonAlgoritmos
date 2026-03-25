def exercicio28(preco_atual, media_mensal):
    if media_mensal < 500 and preco_atual < 30:
        novo_preco = preco_atual * 1.10
    elif media_mensal >= 500 and media_mensal < 1000 and preco_atual >= 30 and preco_atual < 80:
        novo_preco = preco_atual * 1.15
    elif media_mensal >= 1000 and preco_atual >= 80:
        novo_preco = preco_atual * 0.95
    else:
        novo_preco = preco_atual
    print("Novo preço:", novo_preco)

p = float(input("Preço atual: "))
m = float(input("Média mensal: "))

exercicio28(p, m)