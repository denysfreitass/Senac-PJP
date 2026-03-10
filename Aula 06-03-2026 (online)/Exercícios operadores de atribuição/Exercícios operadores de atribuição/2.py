# Leia um contador (int) e um passo (int). Faça contador += passo duas vezes. Mostre o resultado.

contador = int(input("Digite um numero: "))
passos = int(input("Digite um numero de passos: "))
contador += passos
contador += passos
print(f"O contador + o numero de passos duas vezes é : {contador}")
