'''
Desafio 02

Crie uma função que receba dois números e retorne a soma deles. 
'''

def soma_numeros(a, b):
    return a + b

num1 = int(input("Digite um numero: "))
num2 = int(input("DIgite um segundo numero: "))

print(f"A soma dos numeros informados é {soma_numeros(num1, num2)}")