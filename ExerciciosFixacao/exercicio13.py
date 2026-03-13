#Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.

print("Calculadora de salário após uma '%' de aumento")
salario_atual = float(input("Digite seu salário atual: "))
aumento = float(input("Digite a porcentagem de aumento no salario: "))

aumento = aumento * (salario_atual / 100)

novo_salario = salario_atual + aumento

print(f"O seu salário após o aumento da '%' indicada vai acrecentar R$:{aumento:.2f}, ficando R$:{novo_salario:.2f}")

