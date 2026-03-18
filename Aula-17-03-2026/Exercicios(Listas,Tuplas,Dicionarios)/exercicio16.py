#[TUPLE - desafio] Tupla de notas com média (sem alterar a tupla)
#Tarefa: Leia três notas (float) e armazene em uma tupla. Exiba a tupla e a média das notas.
#Use: float(), sum(), len(), print()
#Sem alterar tupla.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

tupla = (nota1, nota2, nota3)
media = sum(tupla) / len(tupla)
print(f"A média das notas {tupla} é : {media:.2f}")