nome = input("Digite seu nome ")
contador = int()
contador2 = int()
curso1 = "Analise de Sistemas"
curso2 = "Direito"
 
op1 = int(input("Você gosta mais de resolver problemas usando lógica do que discutir ideias? 1 - Sim 2- Não"))
if op1 == 1:
    contador = contador + 1
else:
    contador2 = contador2 + 1
op2 = int(input("Você prefere trabalhar mais com computadores do que com pessoas? 1 - Sim 2 - Não"))
if op2 == 1:
    contador = contador + 1
else:
    contador2 = contador2 + 1
 
op3 = int(input("Você gosta de analisar situações e encontrar a solução mais eficiente? 1 - Sim 2 - Não"))
if op3 == 1:
    contador = contador + 1
else:
    contador2 = contador2 + 1
op4 = int(input("Você se sente confortável lendo textos longos e interpretando detalhes? 1 - Sim 2 - Não"))
if op4 == 1:
    contador = contador + 1
else:
    contador2 = contador2 + 1
op5 = int(input("Você gosta de aprender como as coisas funcionam por dentro? 1 - Sim 2 - Não"))
if op3 == 1:
    contador = contador + 1
else:
    contador2 = contador2 + 1

 
if contador > contador2:
    print("O curso escolhido foi: ",curso1)
else:
    print("O curso escolhido foi: ",curso2)