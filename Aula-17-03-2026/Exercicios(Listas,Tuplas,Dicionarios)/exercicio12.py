#[TUPLE] Acessar elementos da tupla
#Tarefa: Leia três frutas e coloque em uma tupla. Depois leia uma fruta e diga se ela está ou não na tupla.
#Orientações: 
#usar in
#usar input()
#tipo: str, tuple
#conceito: operador de pertinência

fruta1 = input("Digite uma fruta: ").title()
fruta2 = input("Digite a segunda fruta: ").title()
fruta3 = input("Digite uma outra fruta: ").title()

tupla = (fruta1, fruta2, fruta3)
print(tupla)

pesquisa = input("Digite o nome de uma fruta para verificar se ela está na tupla: ").capitalize()

if pesquisa in tupla:
    print(f"A {pesquisa}, está na tupla: {tupla}")
else:
    print(f"A fruta pesquisada não pertence a tupla : {tupla}")
    print(type(tupla))