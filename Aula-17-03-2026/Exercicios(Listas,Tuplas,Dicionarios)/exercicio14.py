#[TUPLE] Exibir maior e menor valor
#Tarefa: Leia quatro números inteiros, coloque em uma tupla e exiba o maior e o menor.
#Orientações: 
#funções: max(), min()
#tipos: int, tuple
#conceito: operações básicas de agregação

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))
num4 = int(input("Digite um numero: "))

tupla = (num1, num2, num3, num4)

print(f"O menor valor da tupla é {min(tupla)} e o maior valor é {max(tupla)}")
print(tupla)
print(type(tupla))