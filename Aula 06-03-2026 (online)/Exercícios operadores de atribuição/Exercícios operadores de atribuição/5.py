# Leia estoque (int) e vendidas (int). Atualize com -= e mostre o estoque final.

print("Atividade estoque!")

estoque = int(input("Digite o numero de produtos que você tem em estoque: "))
vendas = int(input("Quantas vendas você realizou? "))

estoque -= vendas
print(f"Seu estoque final é {estoque}!")