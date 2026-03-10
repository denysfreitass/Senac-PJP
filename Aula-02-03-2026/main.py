# exemplo de lista de compras

lista_de_compras = ['maça', 'banana', 'laranja', 'uva']
print("essa é a minha lista de compras: ")
print(lista_de_compras)



#exemplo de lista dicionario 

aluno = { "id":"1",
        "nome":"denys",
         "idade":"20",
         "curso":"jovem programador",
        }

print("dados do aluno: ")
print(aluno)


#exemplo de pesquisa numa lista (dict)

alunos =    [
    { "id": 1,
      "nome":"denys",
      "idade":"20",
      "curso":"jovem programador"
    },
    {"id": 2,
      "nome":"maria",
      "idade":"22",
      "curso":"jovem programador"
    }
    ]

for aluno in alunos:
    if aluno["id"] == 2:
        print("dados do aluno selecionado: ")
        print(aluno)