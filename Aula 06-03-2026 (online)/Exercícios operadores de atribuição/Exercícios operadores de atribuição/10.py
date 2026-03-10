# Leia total (float) e pessoas (int). Use /= para dividir igualmente.

total = float(input("Digite o valor total para dividir igualmente por pessoas: "))
pessoas = int(input("Digite o numero de pessoas: "))

total /= pessoas
print(f"O valor igual para cada pessoa é {total}")