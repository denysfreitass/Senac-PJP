# Leia vidas (int) e perdidas (int). Use vidas -= perdidas.

print("exercicio numero de vidas")

vidas = int(input("Digite o numero inicial de vidas: "))
mortes = int(input("Digite quantas vezes você morreu: "))

vidas -= mortes
print(f"Você ainda tem um total de {vidas} vida!")
