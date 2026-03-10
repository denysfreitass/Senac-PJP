# Leia um número (int), aplique n %= 2 e imprima.
# 0 = par, 1 = ímpar

num_total = int(input("digite um numero: "))
num = num_total
num %= 2

if num == 0:
    print(f"o numero {num_total} é par")
else:
    print(f"o numero {num_total} é impar")
