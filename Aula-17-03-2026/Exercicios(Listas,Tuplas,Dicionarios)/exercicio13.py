#[TUPLE] Contar quantas vezes um número aparece

#Tarefa: Leia quatro números inteiros e crie uma tupla. Depois leia um número e diga quantas vezes ele aparece na tupla.
# Orientações: 
 
#método: tuple.count()
#tipos: int, tuple

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))
num4 = int(input("Digite um numero: "))

tupla = (num1, num2, num3, num4)

verifica = int(input("Digite um numero para verificar sua ocorrencia na tupla: "))
if verifica in tupla:
    tupla.count(verifica)
    print(f"O valor de {verifica}, aparece {tupla.count(verifica)} vezes")
else:
    print("O valor digitado, não aparece nenhuma vez na tupla")
print(tupla)