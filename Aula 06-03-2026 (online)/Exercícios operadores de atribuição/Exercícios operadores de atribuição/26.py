# Leia dois inteiros a e b. Em a: a += b, a *= 2, a %= 7.

num_a = int(input("Digite um valor para 'A': "))
num_b = int(input("Digite um valor para 'B': "))

num_a += num_b
num_a *= 2
num_a %= 7
print(f"O valor final de A, após receber B, multiplicar por 2 e calcular o resto da divisão por 7 é {num_a}")


