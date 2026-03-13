#Leia um número como string e imprima o seu tipo antes e depois de converter para int.

num = input("Digite um numero: ")
print(f"O numero {num} atualmente é do tipo {type(num)}")

num = int(num)
print(f"O numero {num} agora é do tipo {type(num)}")

