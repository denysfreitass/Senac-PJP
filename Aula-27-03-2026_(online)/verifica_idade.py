'''
2. Solicite ao usuário que informe a sua idade e depois exiba se é maior ou menor de idade.

'''

idade = int(input("Digite sua idade: "))

if idade < 18:
    print(f"Você tem {idade}, e é menor de idade!")
else:
    print(f"Você já tem {idade}, e é maior de idade!")