'''
Instruções
Um sistema precisa registrar compras realizadas por clientes.

O programa deverá:

✅ Solicitar o valor de uma compra
✅ Somar os valores informados
✅ Continuar pedindo valores até o usuário digitar 0
✅ Ao final, mostrar:

Total das compras
Quantidade de compras realizadas
Valor médio das compras
Regras
Utilize while
O valor 0 encerra o programa
Não pode usar for
'''
#exercicio solicita pelo professor Wlade dia 31-03-2026 durante a aula.

valor_compras = [] # lista que armazenar os valores

while True: #abrindo o loop para solicitar valores
    valor = float(input("Digite o valor da compra (ou 0 para encerrar): "))
    if valor != 0: #enquanto o valor for diferente de 0, vou adicionando na lista e calculando o total e a média
        valor_compras.append(valor)
        total_compras = sum(valor_compras)
        valor_medio = total_compras / len(valor_compras)
        continue  # volta para o inicio do loop para pedir o próximo valor
    else:
        print("Encerrando calculo das compras..")
        break  #encerra o loop


print(f"Total das compras: R${total_compras:.2f}") 
print(f"Quantidade de compras realizadas: {len(valor_compras)}")
print(f"Valor médio das compras: R${valor_medio:.2f}")

