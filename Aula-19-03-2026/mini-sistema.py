#> Construir um mini-sistema que gerencia catálogo de produtos (lista de tuplas), estoque (em dicionário) e um carrinho de compras (lista). 

#Tarefa: cadastrar 3 produtos.  
#Para cada produto, leia: id (int), nome (string) e preço (float). 
#Armazene cada produto como tuple(id, nome, preco) em uma list() chamada catalogo. 
catalogo = []
estoque = {}

def cadastrar_produtos():
    print("Olá, bem vindo ao mini-sistema de gerenciamento de produtos")

    while True:
        print(f"\nVamos cadastrar o produto ({len(catalogo) + 1})")

        # validação do ID
        while True:
            try:
                id_produto = int(input("Digite o ID: "))
                
                if id_produto < 0:
                    print("O valor do ID não pode ser menor que 0")
                    continue
                
                if any(produto[0] == id_produto for produto in catalogo):
                    print("ID já cadastrado, escolha outro")
                    continue
            except ValueError:
                print("ID deve ser do tipo inteiro, Ex: 1, 2, 3..")
                continue
            break  # ID válido, sai do loop interno

        # cadastro do produto
        nome_produto = input("Digite o nome do produto: ").strip().lower()
        while True:
            try:
                preco_produto = float(input("Digite o preço do produto: "))
                if preco_produto < 0:
                    print("O valor do produto, não pode ser negativo")
                    continue
            except ValueError:
                print("O valor tem que ser do tipo numerico")
                continue
            break
        while True:
            try:
                qnt_produto = int(input("Digite a quantidade em estoque: "))
                if qnt_produto <= 0:
                    print("Para adicionar um item ao catálogo, você deve ter ao menos 1 em estoque!")
                    continue
            except ValueError:
                print("Quantidade deve ser do tipo numerico!")
                continue
            break
        produto = (id_produto, nome_produto, preco_produto)
        catalogo.append(produto)
        estoque[id_produto] = qnt_produto

        print("Produto cadastrado com sucesso!")

        # pergunta se deseja continuar
        continuar = input("Deseja cadastrar outro produto? (sim/não): ").strip().lower()
        if continuar not in ['sim', 's', 'yes', 'y']:
            break  # sai do loop principal e encerra a função

def mostrar_catalogo():
    if not catalogo:
        print("Não há produtos em catalogo")
        return
    print(f"{'ID':<5} {'Nome':<15} {'Preço':<10} {'Quantidade':<10}")
    print('-'* 45)

    for produto in catalogo:
        id_produto = produto[0]
        nome_produto = produto[1]
        preco_produto = produto[2]
        quantidade = estoque[id_produto]
        print(f"{id_produto:<5} {nome_produto.capitalize():<15} R${preco_produto:<10.2f} {quantidade:<10}")
# chamar a função
cadastrar_produtos()
mostrar_catalogo()

# Atualização de Preço (Tupla é imutável -> para alterar precisa recriar a tupla) 
# Tarefa: leia um ID e um percentual de desconto (float). 
# Encontre a tupla do produto correspondente ao id na lista catalogo, recrie a tupla com o preço novo (com o desconto aplicado) e substitua na mesma posição.  
# Mostre o preço antes e depois. 

produto = int(input("Digite um ID para dar desconto ao produto: "))
desconto = float(input("Digite a porcentagem de desconto para o item escolhido: "))

for i, item in enumerate(catalogo):
    if item[0] == produto:
        id, nome, preco = item
        novo_preco = preco * (1 - desconto/100)

        catalogo[i] = (id, nome, novo_preco)
        print(f"{id:<5} {nome:<15} R${novo_preco:<10.2f}")
        break
else:
    print("ID não encontrado no catálogo.")

#4. Montar um carrinho de compras + baixa de estoque
#Crie carrinho = [].
#Leia id e quantidade desejada. Se houver estoque suficiente (estoque[id] >= qtd), adicione ao carrinho a tupla (id, qtd, preco_unit_atual) e desconte do estoque (-= qtd); caso contrário, avise que não há estoque. Exiba o carrinho após cada edição e o estoque atualizado. Use: in, if/else, append, operadores >=, -= Tipos: list(carrinho), dict(estoque), tuple(item do carrinho).


carrinho = []

while True:
    add_prod = int(input("Digite o id do produto desejado: "))
    qnt_prod = int(input("Digite quantas unidades você quer: "))

    if not any(item[0] == add_prod for item in catalogo):
        print("Não existe produto  com este ID!")

    else:
        if qnt_prod > estoque[add_prod]:
            print("Quantidade insuficiente em estoque!")

        else:
            estoque[add_prod] -= qnt_prod
            for item in catalogo:
                if item[0] == add_prod:
                    id_prod, nome_prod, preco_prod = item
                    break

            # 5 — Adiciona ao carrinho
            carrinho.append((id_prod, nome_prod, preco_prod, qnt_prod))

            print("Produto adicionado ao carrinho!")
    continuar_compra = input("Deseja adicionar mais produtos? (sim/não)").strip().lower()
    if continuar_compra in ['sim', 's', 'yes']:
        continue
    else:
        break
def mostrar_carrinho():
    for id_prod, nome_prod, preco_prod, qtd in carrinho:
        print("-" * 30)
        print(f"ID: {id_prod}")
        print(f"Nome: {nome_prod}")
        print(f"Quantidade: {qtd}")
        print(f"Preço unitário: R$ {preco_prod:.2f}")
print(f"-"*10,"Carrinho Compras","-"*10)
mostrar_carrinho()
#5. Remover um item do carrinho e devolver ao estoque
#Leia um id para remoção. Se o id estiver no carrinho, remova a primeira ocorrência e devolva a quantidade ao estoque (+= qtd); caso não esteja, informe. Exiba o carrinho e estoque após a remoção. Use: laço/indíce, pop(), operadores += Tipos: list, dict, tuple

rem_prod = int(input("Digite um ID de produto para remover do carrinho: "))

item_remover = None 

for item in carrinho:
    if item[0] == rem_prod:   
        item_remover = item
        break

if item_remover is None:
    print("O ID informado não se encontra no carrinho!")

else:
    carrinho.remove(item_remover)

    id_prod, nome_prod, preco_prod, qtd_removida = item_remover
    estoque[id_prod] += qtd_removida

    print("Item removido com sucesso!")
print(f"\n")
print(f"-"*5,"Carrinho Compras","-"*5)
mostrar_carrinho()
#6. Resumo final – cálculos e ordenações
#Deve-se exibir:
#Os itens do carrinho (id, qtd, preço unitário).

print("Os itens no carrinho são:")
preco_total = 0 
print(f"-"*5,"Carrinho de Compras","-"*5)
for id_prod, nome_prod, preco_prod, qtd in carrinho:
    print("-" * 30)
    print(f"ID: {id_prod}")
    print(f"Nome: {nome_prod}")
    print(f"Quantidade: {qtd}")
    print(f"Preço unitário: R$ {preco_prod:.2f}")
    preco_total += preco_prod * qtd

#O total a pagar (soma de qtd * preço), com duas casas decimais.
print(f"-"*45)
print(f"O preço total a pagar é: {preco_total:.2f} ")
#O catálogo ordenado por preço (apenas para visualização, sem alterar o catálogo).
catalogo_ordenado = sorted(catalogo, key=lambda produto: produto[2])
print(catalogo_ordenado)
# Use: sum(), len(), soted(iterável, key=...), f-string com formatação :.2f. Tipos: float, list, tuple
