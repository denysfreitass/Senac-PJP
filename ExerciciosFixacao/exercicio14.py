#Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)

print("Conversora de minutos para horas")

tempo = int(input("Digite a quantidade de minutos para converter: "))
horas = tempo // 60
minutos = tempo
minutos %= 60
print(f"A quantidade de minutos informada fica {horas}h{minutos}min")