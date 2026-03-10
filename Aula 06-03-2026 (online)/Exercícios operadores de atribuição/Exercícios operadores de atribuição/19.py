# Leia estoque (int). Subtraia venda com -=, depois reposição com +=, por fim %= 6.

estoque_inicial = int(input("Digite o seu estoque inicial: "))
vendas = int(input("Digite o numero de vendas do dia: "))
reposicao = int(input("Digite o numero de reposição de itens: "))
estoque = estoque_inicial 
estoque -= vendas 
estoque += reposicao 
estoque %= 6
print(f"O seu estoque ao final é {estoque}")

