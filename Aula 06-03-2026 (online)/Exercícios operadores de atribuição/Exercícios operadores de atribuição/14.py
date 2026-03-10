# Leia dias (int). Mantenha apenas os dias restantes após converter para semanas (7 dias) usando %=.


dias_totais = int(input("Digite a quantidade de dias para transformar em semanas: "))
sem = dias_totais
sem /= 7
dias_totais //= 7

print(f"As semanas totais foram {sem:.2f} e os dias restantes {dias_totais}")