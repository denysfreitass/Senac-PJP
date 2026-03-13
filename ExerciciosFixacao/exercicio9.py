#Leia o preço de um produto e imprima o preço com 10% de desconto.

valor_atual = float(input("Digite o valor do produto: "))
valor_desc = valor_atual * 0.9
print(f"Hoje é seu dia de sorte estamos com 10% de desconto e o valor do produto que era R$:{valor_atual}, sai hoje por apenas R$: {valor_desc}")