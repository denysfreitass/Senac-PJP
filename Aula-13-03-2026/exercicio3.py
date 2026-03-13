#[LIST] Atualizar elemento com uma operação

#Tarefa: Crie uma lista com três inteiros. Atualize o último elemento para a soma dos dois primeiros. Exiba a lista.
# Use: int(), input(), indexação lista[i], print()
# Tipos: int, list.
# Conceitos: operadores aritméticos (+), acesso/atribuição por índice.

print("Exercicio atualizar elemento com uma operação")
num1 = int(input("Digite o primeiro numero da lista: "))
num2 = int(input("Digite o segundo numero da lista: "))
num3 = int(input("Digite o terceiro numero da lista: "))

lista = [num1, num2, num3]

somas = lista[0] + lista[1]
lista_atualizada = [num1, num2, somas]
print(f"os valores da lista inicial -> {lista} <- após a operação aritmética (+) dos elemento 1 e elemento 2 da lista, transforam o elemento 3 em {somas} e a lista atualizada fica {lista_atualizada}")

