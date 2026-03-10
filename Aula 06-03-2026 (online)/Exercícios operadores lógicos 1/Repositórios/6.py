# Ambos os números são pares

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))

num1 %= 2 
num2 %= 2

print(num1 == 0 and num2 == 0)