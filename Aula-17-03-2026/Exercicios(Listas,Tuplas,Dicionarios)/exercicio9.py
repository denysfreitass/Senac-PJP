#[DICT - desafio] Atualizar preço e quantidade; calcular o total 

#Tarefa: Leia produto = {"nome": str, "preco": float, "quantidade": int}. Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total = preco * quantidade e exiba.
#Use: float(), int(), input(), acesso/atribuição por chave, print()
#Tipos: str, float, int, dict.
#Conceitos: operadores aritméticos (*, +), atualização de valores no dict.

# Leia produto = {"nome": str,   "preco": float, "quantidade": int}
produto = {"nome: ": "notebook", "preço: ": 3499, "quantidade": 67}
print(produto)

# Aplique aumento percentual ao preço e some 2 unidades na quantidade
valor_acresc = float(input("Digite o valor da porcentagem do aumento: "))
novo_preco = produto['preço: '] + (produto['preço: '] * (valor_acresc / 100))
nova_quantidade = produto["quantidade"] + 2
print(f"O novo preço é {novo_preco} e a nova quantidade é {nova_quantidade}")
produto["preço: "] = novo_preco
produto["quantidade"] = nova_quantidade
print(produto)
#Calcule total = preco * quantidade e exiba.
total = produto['preço: '] * produto['quantidade']
print(f"O valor total do preço x quantidade é {total:.2f}")





