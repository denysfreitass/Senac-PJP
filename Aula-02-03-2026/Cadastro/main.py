
print("Olá, bem vindo ao nosso sistema de cadastro!")
print("Por favor, preencha os campos abaixo para concluir seu cadastro.")

nome = input("Digite seu nome completo: ")
while not nome:
  print("O nome não pode ser vazio.")
  nome = input("Digite seu nome completo: ")

idade = int(input("Digite sua idade: "))
while idade <= 0 or idade > 120:
    print("idade inválida. Por favor, digite uma idade válida.")
    idade = int(input("Digite sua idade: "))
dt_nascimento = input("Digite sua data de nascimento (DDMMAAAA): ")
endereco = input("Digite seu endereço completo: ")
cpf = input("Digite seu CPF sem pontos e hífens: ")
while len(cpf) != 11:
        print("CPF inválido. Por favor, digite um CPF válido com 11 digitos numéricos")
        cpf = input("Digite seu CPF: ")
contato = input("Digite seu telefone para contato com DDD: ")


cpf = str(cpf)
cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

dt_nascimento = str(dt_nascimento)
dt_nascimento_formatada = f"{dt_nascimento[:2]}/{dt_nascimento[2:4]}/{dt_nascimento[4:]}"


                     
print("Cadastro concluído com sucesso!")
print(f"Seus dados são:\nNome: {nome}\nIdade: {idade} anos\nEndereço: {endereco}\nCPF: {cpf_formatado}\nContato: {contato}\nData de Nascimento: {dt_nascimento_formatada}")