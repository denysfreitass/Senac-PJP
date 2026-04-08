'''
Desafio 03

Crie uma função que receba um número e informe se ele é PAR ou ÍMPAR. 
'''
def par_impar(num):
    if num % 2 == 0:
        print(f"O numero {num}, é par!")
    else:
        print(f"O numero {num}, é impar!")

num = int(input("DIgite um numero para verificar se ele é par ou impar: "))

par_impar()