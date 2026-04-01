'''
crie um programa em python que:

peça ao usuário para digitar 10 números inteiros

armazene esses números em uma lista
use um laõ for para percorrer a lista
para cad anúmero, classifique como:

maior que 10
igual a 10
menor que 10
'''

numeros = []
print("Digite 10 números inteiros: ")
for i in range(10):
    num = int(input(f"Digite o numero {i+1}: "))
    numeros.append(num)

for numero in numeros:
    if numero < 10:
        print(f"O numero {numero} é menor que 10")
    elif numero == 10:
        print(f"O numero {numero} é igual a 10")
    else:
        print(f"O numero {numero} é maior que 10")