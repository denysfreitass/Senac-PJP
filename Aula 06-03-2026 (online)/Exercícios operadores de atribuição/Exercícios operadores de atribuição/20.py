# Leia tempo em segundos (int). Converta para minutos inteiros com //= 60 e depois use %= para obter segundos restantes.

segundos_totais = int(input("digite o numero de segundos para converter em minutos: "))
minutos = segundos_totais
minutos //= 60
segundos_totais %= 60

print(f"Os segundos escolhidos em minutos é {minutos}min e sobraram {segundos_totais}segundos")