'''
Desafio 05 
Crie uma função que receba uma string e retorne a quantidade de caracteres que ela possui.
'''

def contar_caracteres(texto):
    return len(texto)

text = input("Digite uma palavra para contar os caracteres: ")

print(f"A palavra {text}, tem {contar_caracteres(text)} caracteres")