'''
atividade: sistema de inventário
criar um módulo de inventário de um novo jogo. O jogador deve ser capaz de adicionar quantos itens encontrar pelo caminho e só parar de organizar a mochila quando desejar.

instruções:
1 - preparação, criar uma lista vazia chamada inventário. 
2- o laço de repetição- utilizar uma função while True, para criar um loop que permita a entrada de multiplos itens.
3- entrada de dados: dentro do loop peça para o usuário digitar um item encontrado ex ( ' escudo ' , 'poção', 'moeda')
4- condições de parada, antes de adicionar o item a lista, verifique se o usuario digitou a palavra 'sair'
    se for 'sair' utilize o comando break para encerrar o loop
5- armazenamento, caso o usuário digitar qualquer outra coisa, utilize o metodo append() para guardar o item ao inventário na lista.
6 - finalizaçao, após sair do loop, o programa deve;
    ordernar a lista em ordem alfabética com .sort()
    exibir a lista completa na tela
    exibir a quantidade de itens coletados, usando a função len()
'''

inventario = []

def adicionar_items():
    while True:
        add_item = input("Digite o nome do item para adicionar ao inventário ou 'sair' para sair no inventário: ").lower()
        if add_item in ['sair']:
            break
        elif not add_item:
            print("ERRO: Você deve digitar o nome do item!") 
        else:
            inventario.append(add_item)

print("Olá, seja bem vindo, vamos organizar seus itens?")
adicionar_items()
inventario.sort()
print(f"\nseu inventário organizado por ordem alfabética é\n")
for i, item in enumerate(inventario, start=1):
    print(f"{i}. {item}")
print(f"\n Você tem {len(inventario)}, items no seu invenátio")
