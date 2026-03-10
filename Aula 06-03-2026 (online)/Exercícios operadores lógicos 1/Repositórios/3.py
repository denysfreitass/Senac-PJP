# Pelo menos um número maior que 50

print("Exercicio numero maior que 50, vamos descobrir se um dos seus números é maior que 50")

num1 = float(input("Digite o numero 1: "))
num2 = float(input("Digite o numero 2: "))

if num1 > 50 or num2 > 50:
    print(f"Parabéns, você digitou um dos números maior que 50 ")
else:
    print(f"Os numeros que você digitou são {num1} e {num2} e nenhum deles é maior que 50! Tente novamente")
