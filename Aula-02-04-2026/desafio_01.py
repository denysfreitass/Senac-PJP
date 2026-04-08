'''
Desafio 01

Crie uma função que receba um nome como parâmetro e exiba a mensagem:

'Bem-vindo, NOME' 
'''

def saudacao(nome):
    print(f"Bem vindo, {nome}")


nome = input("Digite seu nome: ")

saudacao(nome)