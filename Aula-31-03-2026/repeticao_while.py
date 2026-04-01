'''
exemplo do professor

resposta = ''

while resposta != 'sair':
    resposta = input("Digite algo (ou 'sair' para encerrar): ")
    print(f"Você digitou: {resposta}")
'''

#Meu código com while True e if/ else: 
while True:
    resposta = input("DIgite algo ( ou 'sair' para encerrar): ")
    if resposta != 'sair':
        print(f"Você digitou: {resposta}")
        continue
    else:
        print("Saindo...")
        break