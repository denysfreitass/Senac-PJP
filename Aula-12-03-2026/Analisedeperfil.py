#exercicio do coordenador
#fazer um questionario sobre o aluno, e no fim, sugerir algum curso, conforme suas respostas
#minha equipe escolhei os cursos de direito e analise e desenvolvimento de sistemas


print("Olá, bem vindo ao questionario de orientação vocacional!")
nome = input("Qual o seu nome? ")
idade = int(input("Digite a sua idade: "))
print("Agora, responda as perguntas com 1 para sim e 2 para não! ")

#perguntas

op_1 = int(input("Você gosta de discutir problemas complexos e defender  suas opnião? ")) #neutra
op_2 = int(input("Você gosta de tecnologia? ")) #sugestiva a ADS
op_3 = int(input("Você prefere trabalhar com computadores do que com pessoas? ")) #se não, sugere direito
op_4 = int(input("Você tem interesse em saber mais sobre leis e direitos? ")) #sugestiva a direito
op_5 = int(input("Você gosta de resolver problemas lógicos? ")) #sugestiva a ADS

#analise das respostas

if op_2 == 1 and op_3 == 1 and op_5 == 1:
    print(f"Olá, {nome}, com base nas suas respostas, sugerimos que você considere o curso de Análise e desenvolvimento de sistemas, pois você tende a gosta de tecnologia e prefere trabalhar com computadores. além de gostar de resolver problemas lógicos")
elif op_1 == 1 and op_4 ==1 and op_3 == 2:
    print(f"Olá, {nome}, com base nas suas respostas, sugerimos que você considere o curso de Direito, pois você gosta de discutir problemas complexos e defender suas opiniões, além de ter interesse em saber mais sobre leis e direitos.")
