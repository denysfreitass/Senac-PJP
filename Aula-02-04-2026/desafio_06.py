'''
Desafio 06 
Crie uma função que receba uma lista de números e retorne a média dos valores.
'''

def media_valores(lista):
    return sum(lista) / len(lista)

numeros = []
while True:
    num = input("Digite um numero para adicionar a lista ou 'sair' para encerrar: ").strip().lower()
    if not num:
        print("Você precisa digitar 'sair' ou algum numero para adicionar a lista!")
        continue
    elif num == 'sair':
        print("Encerrando.. ")
        if not numeros:
            print(f"Você não tinha nenhum valor na lista!")
        else:
            print(f"A media dos valores da lista é {media_valores(numeros)}")
            break
    else:
        try:
            numeros.append(int(num))
        except ValueError:
            print("Digite apenas números ou 'sair'!")
            continue

    
        