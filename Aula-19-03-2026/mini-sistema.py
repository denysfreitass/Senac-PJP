#> Construir um mini-sistema que gerencia catálogo de produtos (lista de tuplas), estoque (em dicionário) e um carrinho de compras (lista). 

#Tarefa: cadastrar 3 produtos.  
#Para cada produto, leia: id (int), nome (string) e preço (float). 
#Armazene cada produto como tuple(id, nome, preco) em uma list() chamada catalogo. 

print("Bem vindo ao gerenciador de produtos, abaixo iremos adicionar alguns produtos em estoque")
cadastro_id_1 = int(input("Digite o ID do produto cadastrado: "))
cadastro_nome_1 = input("Digite o nome do produto: ").title()
cadastro_preco_1 = float(input("Digite o preço do produto: "))
cadastro_estoque_1 = int(input("Digite a quantidade em estoque: "))
print("Cadastrar produto 2")
cadastro_id_2 = int(input("Digite o ID do produto cadastrado: "))
cadastro_nome_2 = input("Digite o nome do produto: ").title()
cadastro_preco_2 = float(input("Digite o preço do produto: "))
cadastro_estoque_2 = int(input("Digite a quantidade em estoque: "))
print("Cadastrar produto 3")
cadastro_id_3 = int(input("Digite o ID do produto cadastrado: "))
cadastro_nome_3 = input("Digite o nome do produto: ").title()
cadastro_preco_3 = float(input("Digite o preço do produto: "))
cadastro_estoque_3 = int(input("Digite a quantidade em estoque: "))

catalogo = [
    (cadastro_id_1, cadastro_nome_1, cadastro_preco_1),
    (cadastro_id_2, cadastro_nome_2, cadastro_preco_2),
    (cadastro_id_3, cadastro_nome_3, cadastro_preco_3)
]

print(f"Até agora os produtos em catalogo são {catalogo}")
print(type(catalogo))

#Estoque por produto 
# O estoque dos produtos será um dicionário. 
#Tarefa: crie um dicionário estoque associando id (produto) -> quantidade (int). 
#Para cada produto (tupla) do catálogo (lista), leia a quantidade inicial e salve em estoque[id]. 

estoque_inicial = dict([
    (catalogo[0][0], cadastro_estoque_1),
    (catalogo[1][0], cadastro_estoque_2),
    (catalogo[2][0], cadastro_estoque_3)
])

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
        print(catalogo)
        break
else:
    print("ID não encontrado no catálogo.")

#4. Montar um carrinho de compras + baixa de estoque
#Crie carrinho = [].
#Leia id e quantidade desejada. Se houver estoque suficiente (estoque[id] >= qtd), adicione ao carrinho a tupla (id, qtd, preco_unit_atual) e desconte do estoque (-= qtd); caso contrário, avise que não há estoque. Exiba o carrinho após cada edição e o estoque atualizado. Use: in, if/else, append, operadores >=, -= Tipos: list(carrinho), dict(estoque), tuple(item do carrinho).


carrinho = []

add_prod = int(input("Digite o id do produto desejado: "))
qnt_prod = int(input("Digite quantas unidades você quer: "))

if add_prod not in estoque_inicial:
    print("Não existe produto  com este ID!")

else:
    if qnt_prod > estoque_inicial[add_prod]:
        print("Quantidade insuficiente em estoque!")

    else:
        estoque_inicial[add_prod] -= qnt_prod
        for item in catalogo:
            if item[0] == add_prod:
                id_prod, nome_prod, preco_prod = item
                break

        # 5 — Adiciona ao carrinho
        carrinho.append((id_prod, nome_prod, preco_prod, qnt_prod))

        print("Produto adicionado ao carrinho!")


for id_prod, nome_prod, preco_prod, qtd in carrinho:
    print("-" * 30)
    print(f"ID: {id_prod}")
    print(f"Nome: {nome_prod}")
    print(f"Quantidade: {qtd}")
    print(f"Preço unitário: R$ {preco_prod:.2f}")
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
    estoque_inicial[id_prod] += qtd_removida

    print("Item removido com sucesso!")

#6. Resumo final – cálculos e ordenações
#Deve-se exibir:
#Os itens do carrinho (id, qtd, preço unitário).

print("Os itens no carrinho são:")
preco_total = 0 

for id_prod, nome_prod, preco_prod, qtd in carrinho:
    print("-" * 30)
    print(f"ID: {id_prod}")
    print(f"Nome: {nome_prod}")
    print(f"Quantidade: {qtd}")
    print(f"Preço unitário: R$ {preco_prod:.2f}")
    preco_total += preco_prod * qtd

#O total a pagar (soma de qtd * preço), com duas casas decimais.
print(f"O preço total a pagar é: {preco_total} ")
#O catálogo ordenado por preço (apenas para visualização, sem alterar o catálogo).
print(f"O catálogo ordenado por preço é {sorted(catalogo[2])}")
# Use: sum(), len(), soted(iterável, key=...), f-string com formatação :.2f. Tipos: float, list, tuple
