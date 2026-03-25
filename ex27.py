def exercicio27(voltas, extensao, tempo):
    distancia_km = (extensao * voltas) / 1000
    tempo_horas = tempo / 60
    velocidade_media = distancia_km / tempo_horas
    print("Velocidade média:", velocidade_media, "km/h")

v = int(input("Número de voltas: "))
e = float(input("Extensão do circuito (m): "))
t = float(input("Tempo de duração (min): "))

exercicio27(v, e, t)