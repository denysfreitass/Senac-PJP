# Leia orçamento (float) e gasto (float). Faça orcamento -= gasto.

print("Vamos calcular o gasto dessa compra e ver o seu orçamento final")

grana = int(input("Digite o valor do seu orçamento inicial: "))
gasto = int(input("Digite o valor dos produtos: "))

grana -= gasto
print(f"O seu orçamento final com os gastos ficará: {grana}")