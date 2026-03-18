#Criar e exibir uma tupla simples

#Tarefa: Leia dois nomes do usuário e coloque-os em uma tupla. Depois exiba a tupla e o tipo dela.
#Orientações: 
#usar input(), print(), type()
#usar tupla no formato (valor1, valor2)
#tipo trabalhado: str, tuple

nome1 = input("Digite o primeiro nome: ").title()
nome2 = input("Digite o segundo nome: ").title()

tupla = (nome1, nome2)
print(tupla)
print(type(tupla))