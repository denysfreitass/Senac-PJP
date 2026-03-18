#[DICT] Criar e exibir dicionário de aluno

#Tarefa: Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo.
# Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type()
# Tipos: str, int, dict.
# Conceitos: mapeamento chave-valor, criação e exibição.

#ler nome e idade do aluno

nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
#criando lista aluno com nome e idade
aluno = {"nome: ": nome, "idade: ":idade}
print(aluno)
#exibindo o tipo do dicionario
print(type(aluno))

pesquisar = input("Digite o nome para pesquisar: ")                                                           #nomedalista["chave"]    
if pesquisar == aluno["nome: "]:  #aqui eu vejo se o nome informado no pesquisar é igual a algum nome na lista aluno["nome: "]
    print(f"Os dados encontrados para o aluno pesquisado são: \n Dados do Aluno \n Nome: {aluno['nome: ']} | Idade: {aluno['idade: ']}")
else:
    print("Aluno não localizado")