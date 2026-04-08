'''
Desafio 04

Crie uma função que receba uma lista de números e retorne o maior número da lista. 
'''

def mostrar_maior(numeros):
    if not numeros[0]:
        print("Você não tem numeros na lista!")
    else:
        print(f"O maior numero da sua lista é: {max(numeros)}\n e a lista completa é {numeros}")

numeros = []

while True:
    num = input("Digite um numero para adicionar a lista ou 'Sair' para encerrar: ")
    if num == 'sair':
        break
    else:
        numeros.append(num)
        continue

mostrar_maior(numeros)