#[LIST - desafio] Fila: chegadas, prioridade e atendimento

#Tarefa: Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.
# Use: input(), extend(), insert(), pop(), print()
# Tipos: str, list.
# Conceitos: estrutura de fila, operações de inserção/remoção, ordem.

print("Exercicio 5, adicionar 2 nomes na lista com extend, ler um cliente prioritário e ordenar a lista com o nome do prioritário no elemento 1 da tabela")

#inicie fila
fila = ["ana", "Bruno"]
#lendo 2 nomes
cliente1 = input("Digite seu nome: ")
cliente2 = input("Digite seu nome: ")
#adicionando com exted
fila.extend([cliente1, cliente2])
print(f"Fila atualizada: {fila}")
#lendo cliente prioritario
cliente_pri = input("Digite o nome do cliente prioritário: ")
fila.insert(0, cliente_pri) #fila.insert (0 <- posição 1, variavelcomnome ) 
print(f"Fila com cliente prioritário: {fila}")
atendido = fila.pop(0) #fila.pop(0) -> remove o primeiro cliente da fila
print(f"Cliente atendido: {atendido}") 
print(f"Fila atualizada após atendimento: {fila}")

