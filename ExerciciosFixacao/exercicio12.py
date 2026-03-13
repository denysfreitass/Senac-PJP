#Leia 3 notas (float) e imprima a média com duas casas decimais.

print("Hoje vamos calcular sua média do semestre!")
nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))
nota3 = float(input("Digite a nota da prova 3: "))

media = (nota1 + nota2 + nota3) / 3
print(f"Sua média do semestre é: {media:.2f}")