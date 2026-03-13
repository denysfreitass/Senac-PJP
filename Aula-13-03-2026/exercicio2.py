#[LIST] Remova um número se ele existir

#Tarefa: Leia quatro inteiros e crie uma lista. Leia um valor alvo e remova se ele estiver na lista. Mostre o tamanho antes e depois.
# Use: int(), input(), in, remove(), len(), print()
# Tipos: int, list.
# Conceitos: teste de pertencimento, tratamento simples de remoção, função len().


print("Exercicio 2 sobre listas, ler 4 numeros inteiros e criar uma lista, ler um valor alvo e remova se ele estiver na lista")

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
num4 = int(input("Digite o quarto numero: "))

lista = [num1, num2, num3, num4]
print(lista)
print(len(lista))

valor = int(input("Digite o numero para remover: "))

if valor in lista:
    lista.remove(valor)
    print(lista)
    print(len(lista))
else:
    print(f"O numero digitado não pertencia a lista: {lista}")
