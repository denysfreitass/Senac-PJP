#Adicionar uma nova chave nota
#Tarefa: Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.
#Use: float(), input(), atribuição dict["nota"] = valor, print()
#Tipos: float, dict.
#  Conceitos: atualização/adição de chave, tipos numéricos.


#lista inicial com nome e idade
alunos = {"Nome:":"Denys", "idade:": 29}
print(alunos)
nota = float(input("Digite uma nota: "))
alunos["nota"] =  nota
print(alunos)
