'''
6. Faça uma calculadora simples contendo as operações: soma, subtração, divisão e multiplicação. Solicite ao usuário que informe dois número e que informe também a operação que deseja realizar (+, -, /, *) e depois exiba o resultado.

'''

print(f"Calculadora simples de 2 numeros\n")

while True:
    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
    except ValueError:
        print("Por favor, digite apenas numeros!")
        continue
    print("\nAs operações possiveis são, soma (+), subtração (-), divisão (/) e multiplicação (*)!")
    operacao = input("\nDigite a operação que você quer realizar (+, -, /, *): ").strip()


    if operacao == '+':
        print(f"O resultado da soma do {num1} + {num2} é :  {num1 + num2}")
    elif operacao == '-':
        print(f"O resultado da subtração do {num1} - {num2} é : {num1 - num2}")
    elif operacao == '/':
        if num2 == 0:
            print("Divisão não permitida!")
            continue
        else:
            print(f"O resultado da divisão do {num1} / {num2} é : {num1 / num2}")
    elif operacao == '*':
        print(f"O resultado da multiplicação do {num1} * {num2} é : {num1 * num2}")
    else:
        print("Você digitou um comando inválido!")

    continuar = input("Deseja fazer outra operação? Sim/Não: ").lower()
    if continuar in ['sim', 's']:
        continue
    else:
        print("Obrigado por usar a calculadora\nSaindo...")
        break