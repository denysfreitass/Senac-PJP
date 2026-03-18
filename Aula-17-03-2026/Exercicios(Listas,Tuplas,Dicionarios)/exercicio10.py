#[DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes

#Tarefa: Comece com agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}. 
#Adicionar um novo contato (nome→telefone)
#Atualizar o telefone de um contato informado (se existir)
#Remover um contato pelo nome (se existir)
# Exibir a lista ordenada de nomes de contatos
# Tipos: str, dict, list (para a lista ordenada, se desejar armazenar).Conceitos: CRUD em dicionários, teste de existência, ordenação de chaves.Use: input(), acesso/atribuição agenda[nome] = tel, in, pop(), sorted(agenda.keys()), print()

# agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}

agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}
nome = input("Digite o nome do aluno: ").title()
telefone = input("Digite o contato do aluno: ")

agenda.update({nome: telefone})
print(agenda)

#Pedir o nome para atualizar
atualizar = input("Digite o nome do aluno que você quer atualizar o contato: ").strip().capitalize()

#Verificar se o nome existe na agenda
if atualizar in agenda:
    novo_contato = input(f"Digite o novo contato para {atualizar}: ")
    
    # Atualizando diretamente pela chave
    agenda[atualizar] = novo_contato
    print(f"Contato de {atualizar} atualizado com sucesso!")
else:
    print(f"Erro: O aluno '{atualizar}' não foi encontrado na agenda.")

print(f"Agenda atual: {agenda}")

#pedir o nome do contato para remover
remover = input("Digite o nome do aluno que você quer remover da agenda: ").strip().capitalize()

if remover in agenda:
    agenda.pop(remover)
    print(agenda)
else:
    print("O nome do aluno informado. não existe na agenda!")

print(sorted(agenda))