#[TUPLE - desafio] Organizar valores sem mexer na tupla original
#Tarefa: Leia quatro números em uma tupla e exiba: 
# a tupla original
# uma lista ordenada apenas para visualização
# o tipo da variável ordenada
# Objetivo: mostrar diferença entre tupla e lista sem precisar modificar nada.Use: sorted(), print(), type()

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))
num4 = int(input("Digite um numero: "))

tupla = (num1, num2, num3, num4)
print(tupla) # a tupla original
print(sorted(tupla)) # uma lista ordenada apenas para visualização
print(type(tupla))
print(type(sorted(tupla)))