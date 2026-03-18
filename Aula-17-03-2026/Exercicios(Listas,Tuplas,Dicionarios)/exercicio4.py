#[LIST - desafio] Notas: subtituir a menor nota, ordenar e recalcular a média

#Tarefa: Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por uma nova informada. Ordene a lista e mostre a nova média.
# Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()
# Tipos: float, list.
# Conceitos: mutabilidade, ordenação in-place, média aritmética.


print("Exercicio 4 leitura de 3 notas, mostrar média, substituir uma das notas, reordenar lista e mostrar nova média")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda note: "))
nota3 = float(input("Digite a terceira nota: "))

lista1 = [nota1, nota2, nota3]
media = sum(lista1) / len(lista1)

menor_nota = min(lista1)

print(f"A média das notas atuais é {media:.2f}")
print(f"Agora, vamos substituir a menor nota {menor_nota} pela nota da recuperação!")
notarec = float(input("Digite a nota da recuperação: "))

indice = lista1.index(menor_nota)
lista1[indice] = notarec

lista1.sort()
nova_media = sum(lista1) / len(lista1)
print(f"A lista ordenada e atualizada é {lista1} e a nova média ficou {nova_media:.2f}")
