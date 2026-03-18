# listas - list
#definição: coleção ordenada, mutável, permite elementos duplicados


 #indices [   0,      1,       2, ....]  
frutas  = ["maça", "banana", "uva"]
numero = [1, 2, 3, 4, 5]

#acessando elementos
print("Primeira fruta: ", frutas[0])
print("Ultima fruta: ", frutas[2])

#fatiamento (slicing)
print("Frutas do indice 0 ao 1: ", frutas[0:2]) #frutas[0:2] -> do indice 0 até o indice 1 (2-1)
print("Frutas do indice 1 em diante: ", frutas[1:]) #fr

#verificar se um item está na lista
print("Tem 'maça' na lista ?: " in frutas)


#alterar elementos
frutas[1] = "bana caturra"
print("lista após alteração: ",frutas)

#outras operações uteis
print("Lista original 'numeros': ", numero)
print("Soma dos numeros: ", sum(numero))

#tuplas - tuple
#definição: coleção ordenada, imutável, permite elementos duplicados

coordenadas = (10, 20)
dias = ("segunda", "terça", "quarta", "quinta", "sexta")

#acessando elementos
print("x: ", coordenadas[0], "| y: ", coordenadas[1])

#slicing ( fatiamento) em tuplas
print("Primeiros 3 dias: " , dias[0:3])

#tamanho da tupla
print("Quantidade de dias: ", len(dias))

#verificar se um item está na tupla
print("Tem 'segunda' na tupla ?: " in dias)

#contagem e indice em tuplas
print("Quantas vezes 'segunda' aparece na tupla ?: ", dias.count("segunda"))
print("Indice da primeira ocorrência de 'quarta' na tupla: ", dias.index("quarta"))

#dicionarios - dict
#criando dicinarios
aluna = {"id": 1, "nome": "Denys", "nota: ": 9.2}
pessoa = {"nome": "Denys", "idade: ": 29}

#acessasr valores por chaves
print("Nome da aluna: ", aluna["nome"])

#adicionar e alterar chaves/valores
pessoa["cidade"] = "Florianópolis" #adicionando nova chave/valor
pessoa["idade"] = 28 #alterando valor da chave existente

#remover chave
removido = pessoa.pop("idade") #remove a chave "idade" e retorna o valor removido
print("valor removido(idade): ", removido)
print("Após pop('idade'): ", pessoa)

#tamanho
print("Quantidade de chaves no dicionário aluna: ", len(aluna))

#alterar varias chaves/valores com update
aluna.update({"nota: ": 9.5, "cidade": "Florianópolis"})
print("Dicionário aluna atualizado: ", aluna)

