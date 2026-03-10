# Senha correta

senha = 654321
print("Olá, bem vindo ao login do usuario ")
senha2 = int(input("Digite a senha para acessar o sistema: "))
if senha2 != senha:
    print("Senha errada!")
else:
    print("Acesso autorizado!")
