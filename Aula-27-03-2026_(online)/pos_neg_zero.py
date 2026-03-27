'''
1. Solicite ao usuário que informe um número e depois exiba se o número é positivo, negativo ou zero.

'''

num = int(input("Digite um numero: "))

if num < 0:
    print(f"O {num} é negativo!")
elif num == 0:
    print(f"Você digitou zero")
else:
    print(f"Você escolheu {num} e ele é positivo")