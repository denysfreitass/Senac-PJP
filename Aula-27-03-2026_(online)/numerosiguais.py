'''
5. Solicite ao usuário que informe dois números e depois exiba qual número é maior ou se são iguais.
'''


num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

numeros = [num1, num2]

if numeros[0] == numeros[1]:
    print(f"Os numeros {num1:.2f} e {num2:.2f} são iguais!")
elif numeros[0] > numeros[1]:
    print(f"O numero {num1:.2f} é maior que {num2:.2f}!")
else:
    print(f"O numero {num2:.2f} é maior que {num1:.2f}!")
     