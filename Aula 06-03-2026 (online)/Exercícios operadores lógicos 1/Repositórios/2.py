# Idade entre 18 e 30

# descobrir se a idade é entre 18 e 30
idade = int(input("Digite uma idade: "))
while idade <= 18 or idade >= 30:
    print(f"Você digitou {idade}, que está fora dos parametros de 18 a 30 anos")
    idade = int(input("Digite uma nova idade: "))
else:
    print(f"Parabéns, sua idade é {idade} e está entre os parametros definidos de ser entre 18 e 30")