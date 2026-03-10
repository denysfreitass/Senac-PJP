# Leia base (float). Aplique *= 1.05 (aumento 5%), depois -= 2 (taxa), depois /= 2.

base_inicial = float(input("Digite um valor base: "))
base = base_inicial
base *= 1.05
print(f"O valor {base_inicial} base com taxa de 5% fica {base}")
base -= 2
print(f"Diminuindo a taxa de 2 o valor fica {base}")
base /= 2
print(f"Dividindo o resultado por 2, ficam {base}")