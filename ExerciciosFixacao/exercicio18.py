#Leia um nome e uma nota (float), com uma casa decimal, e imprima:
#Aluno <nome> ficou com nota <nota> 

nome = input("Digite o seu nome: ")
nota = float(input("Digite sua nota: "))
print(f"Aluno {nome} ficou com nota {nota:.1f}")

