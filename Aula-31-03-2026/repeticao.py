'''
exemplo 1

'''

for i in range(5):
    print(i)


'''
exemplo 2

'''

alunos = ["Denys", "Maria", "João", "Ana", "Carlos"]

for i in range(len(alunos)):
    print(f"Aluno {i+1}: {alunos[i]}\n")

'''
exemplo 3, pegando o nome e a nota de cada aluno e verificando se ele aprovou ou reprovou

'''

alunos = {'Denys': 9.2, 'Joao': 8.5, 'Maria': 5.0, 'Ana': 4.6}
for aluno, nota in alunos.items():
    print(f"Aluno: {aluno} | Nota : {nota}")
    if nota >= 7:
        print("Parabéns, você está aprovado!\n")
    else:
        print("Infelizmente, você reprovou!\n")

alunos = {'Denys': 9.2, 'Joao': 8.5, 'Maria': 5.0, 'Ana': 4.6}
for aluno, nota in alunos.items():
    if nota <= 7:
        print(f"Aluno: {aluno} | Nota: {nota}")
        print("Infelizmente, você reprovou!\n")