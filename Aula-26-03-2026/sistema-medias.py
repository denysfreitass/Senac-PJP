'''
objetivo: desenvolver um sistema que automatize o cálculo de médias escolares, permitindo inserção de um numero de notas ilimitadas e fornecendo status final do aluno

você deve criar um programa que ajude o professor a lançar notas. O sistema deve ser flexivel o professor pode lançar 2 notas, 5 ou 10 e o programa deve calcular a média aritmédica corretamente ao final

1 - iniciar uma lista de notas vazia chamada notas para armazenar as notas que o professor incluir
iniciar um laço while True, para que o professor possa incluir as notas que quiser, detalhe, notas podem ser decimais então utilize float

2 - condições de saida
criar uma regra para se o professor digitar uma nota negativa o loot deve ser encerrado com o comando break

3- processamento de dados
 usar a função sum(), len() e calcular a média

4- lógica de aprovação
se a média for maior ou igual a 7 - exibir 'aprovado'
se a média for menor que 7 - exibir 'recuperação'

5- mostrar a lista de todas as notas
6- mostrar a media final formatada em 2 casas decimais
'''

notas = []
def adicionar_notas():
    while True:
        nota = float(input(f"Digite a nota {len(notas) + 1}: "))
        
        if nota < 0:
            print("A nota deve ser maior que 0!")
            continue
        
        notas.append(nota)

        continuar = input("Deseja adicionar outra nota? (Sim/Não): ").strip().lower()
        if continuar not in ['sim', 's']:
            break

print("Olá, nesse sistema você poderá calcular a média de notas de um aluno e ver a sua situação final!")

adicionar_notas()

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"A média das {notas}, é {media:.2f}")
    
    if media < 7:
        print(f"O aluno tirou média {media:.2f}, e ficou em RECUPERAÇÃO!")
    else:
        print(f"O aluno tirou a média {media:.2f}, e está APROVADO!")
else:
    print("Nenhuma nota foi adicionada.")

print(notas)