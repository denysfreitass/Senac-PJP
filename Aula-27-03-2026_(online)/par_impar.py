'''
Listas de exercícios - Estruturas de Controle

4. Solicite ao usuário que informe um número e depois exiba se é par ou ímpar.
'''

num = int(input("Digite um numero, para saber se é par ou impar: "))

if (num % 2) == 0:
    print(f"O numero {num} é par!")
else:
    print(f"O numero {num} é impar!")