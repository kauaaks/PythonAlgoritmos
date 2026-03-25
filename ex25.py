def exercicio25():
    inicio_h = int(input("Hora inicial: "))
    inicio_m = int(input("Minuto inicial: "))
    fim_h = int(input("Hora final: "))
    fim_m = int(input("Minuto final: "))
    inicio_total = inicio_h * 60 + inicio_m
    fim_total = fim_h * 60 + fim_m
    if fim_total < inicio_total:
        fim_total += 24 * 60
    duracao = fim_total - inicio_total
    horas = duracao // 60
    minutos = duracao % 60
    print(f"Duração do jogo: {horas}h {minutos}min")

exercicio25()