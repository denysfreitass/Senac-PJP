'''

Desafio 07 
Crie uma função que receba uma palavra e verifique se ela é um palíndromo
(lê igual de trás para frente).

'''

def palindromo(palavra):
    palavra_limpa = palavra.lower().replace(' ',"")
    if palavra_limpa == palavra_limpa[::-1]:
        print(f"A {palavra}, é um palindromo!")
    else:
        print(f"A {palavra}, não é um palindromo!")

palindromo('ana')
palindromo('joao')
