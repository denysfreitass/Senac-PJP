#exemplo integrando todos os elementos vistos até agora

#objetivo calcular e classificar o IMG de sorma simplificada
#nome, peso, altura 
#img = peso / altura ** 2

print("Olá, bem vindo a calculadora de IMC")
nome = input("Digite o seu nome: ")
while not nome or not nome.isalpha():
    print("Por favor, digite um nome válido! ")
    nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso: "))
while not peso or peso <= 0:
    print("Por favor, digite um peso válido!")
    peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura em metros: "))
while not altura or altura <= 0 or altura > 3:
    print("Por favor, digite a sua altura em metros!")
    altura = float(input("Digite sua altura: "))

#calculando o IMC
imc = peso / (altura ** 2)
print(f"Olá {nome}, o seu IMC é {imc:.2f} ")

#faixas de classificação do IMC
baixo_peso = imc < 18.5
peso_normal = imc >= 18.5 and imc < 25
sobrepeso = imc >= 25 and imc < 30
obesidade = imc >= 30

#selecionando em qual faixa ficou o IMC informado
if imc < 18.5:
    print("Você está abaixo do peso ideal:") 
elif imc > 18.5 and imc <= 25:
    print("Parabéns, seu peso está ideal!") 
elif imc > 25 and imc < 30:
    print("cuidado, você está com sobrepeso!")
else:
    print("Cuidado, você está com obesidade!") 



#exercicios da aula 10-03-2026
#listas, tuplas e dicionários

#listas
