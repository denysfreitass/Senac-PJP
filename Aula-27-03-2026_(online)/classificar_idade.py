'''
3. Solicite ao usuário que informe a sua idade e depois classifique em:
a. Menor ou igual a 11 anos = criança.
b. Maior do que 11 e menor ou igual a 17 = adolescente.
c. Maior do que 17 e menor ou igual a 59 = adulto
d. Maior do que 59 = idoso.

'''

idade = int(input("Digite sua idade: "))

if idade <= 11:
    print("Você ainda é criança!")
elif idade <= 17:
    print("Você é adolescente")
elif idade <= 59:
    print("Você é adulto")
else:
    print("Você é idoso")  