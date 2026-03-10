# Número NÃO é zero

num = int(input("Digite um numero: "))
while num == 0:
    print("Você digitou um numero igual a 0! ")
    num = int(input("Digite outro numero: "))
else:
    print("O seu número é diferente de 0")