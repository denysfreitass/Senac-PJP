''' 
classificação de temperatura
peça que o usuario que digite a temperatura atual e classifique?

<10 °c -> Muito frio
10 a 24°C -> Agrádavel 
25 a 30°C -> Quente
30°C -> Muito quente


'''
''' Algoritmo em linguagem natural

1 - iniciar o algoritmo
2 - solicitar a temperatura ao usuario
3- verificar a temperatura
se temperatura menor que 10
    exibir que o clima está muito frio
se temperatura for igual ou maior que 10 e menor ou igual a 24
    exibir que o clima está agradável
se temperatura for maior que 25 e menor que 30
    exibir que está quente
senão:
    exibir que está muito quente

'''

print("Bem vindo a classificação de temperatura")
temp = float(input("Digite a temperatura atual em °C "))

if temp < 10:
    print("O clima está muito frio")
elif temp < 24:
    print("O clima atualmente está agrádavel")
elif temp < 30:
    print("O clima está quente!")
else:
    print("O clima hoje está muito quente!")
    