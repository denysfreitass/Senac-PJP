#[DICT] Remover uma chave com segurança
#Tarefa: Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" se existir, sem gerar erro. Mostre antes e depois.
#Use: input(), float(), dict.pop("chave", valor_padrao), print()
#Tipos: str, float, dict.
#  Conceitos: remoção segura, estado antes/depois.

#produto    "nome": string,   "preço": "float"
produto = {"nome": "Notebook", "preço": 3499}
print(produto)
valor_desc = 0 
desc = input("O produto tem desconto? (sim/não): ").strip().lower()
match desc:  #procura o "match" na variavel indicada ->> 'desc'
    case 'sim':  #caso , for 'sim' <-- 
        valor_desc = float(input("Digite quantos porcento de desconto: "))  #le um valor
        produto["desconto"] = valor_desc #cria a chave 'desconto' no dic 'produto' e da valor = 'input' anterior
        print(produto) #mostra o novo dicionario
    case 'não' | "nao" | "n":      # verifica se for 'não' ou qualquer outra 
        print("O valor não tem desconto: ")  #informa que não tem desconto
    case _:  #se não bater com nenhum das alternativas anteriores
        print("Resposta invalida.") #resposta invalida
valor_padrao = produto["preço"]    #da o valor da chave 'preço' do dicionario produto para variavel 'valor_padrao'
valor_final = valor_padrao - ( valor_padrao * (valor_desc / 100)) #cria a variavel valor_final e faz o calculo matematico 
print(f"O valor padrão é {valor_padrao} e o valor com desconto é {valor_final}")
print(produto) 
remover = produto.pop("desconto", "chave não encontrada") #variavel remover = 'lista'.pop('chavepararemover', 'se não tiver, mostra isso')
print(f"Chave 'desconto' removida com sucesso: {remover}") #printa que conseguiu remover com sucesso e mostra o que foi removido
print(produto) # mostrando a tabela após remover com o pop de forma segura
