'''
crie um programa que recebe uma nota ( 0 a 10 ) e classifique:
<5 - reprovado
5  6.9 - recuperação
7 a 8.9 - aprovado
9 a 10 - aprovado com excelencia

Algoritmo em linguagem normal 
e código python

'''
''' Algoritmo normal 

1- iniciar o algoritmo
2- ler uma nota
se nota for menor que 5
    exibir que o aluno está reprovado
se nota igual ou maior que 5 e menor ou igual a 6.9
    exibir que o aluno está em recuperação
se nota for igual ou maior que 7 e menor ou igual a 8.9
    exibir que o aluno está aprovado
senão
    exibir que o aluno está aprovado com excelencia


'''      
print("Olá, vamos ver a sua situação atual conforme sua nota!")

nota = float(input("Digite sua nota: "))

while True:
    if nota <= 0 or nota > 10:
        print("Digite uma nota válida!")
        nota = float(input("Digite sua nota: "))
    else:
        break

if nota < 5:
    print(f"Infelizmente sua nota foi {nota:.2f}, e você está REPROVADO!")
elif nota >= 5 and nota <= 6.9:
    print(f"Olá, sua nota é {nota:.2f}, e você ficou em RECUPERAÇÃO!")
elif nota >= 7 and nota <= 8.9:
    print(f"Parabéns, sua nota foi {nota:.2f}, e você está APROVADO!")
else:
    print(f"Excelente, sua nota foi {nota:.2f}, e você está APROVADO COM EXCELENCIA!")