# Leia metros (int). Converta para km inteiros com //= 1000 e guarde metros restantes com %= (em outra variável).


metros_totais = int(input("digite o numero de metros para converter em minutos: "))
quilometros = metros_totais
quilometros //= 1000
metros_totais %= 1000

print(f"Os metros escolhidos em quilometros é {quilometros}km e sobraram {metros_totais}metros")