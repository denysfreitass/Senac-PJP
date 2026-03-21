import sqlite3

# ===== Conexão com banco de dados =====
conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

# ===== Criar tabela caso não exista =====
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco REAL,
    quantidade INTEGER
)
""")
conexao.commit()

# ===== Listas e dicionários =====
catalogo = []
estoque = {}

# ===== Importa produtos já salvos no banco =====
cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
for id_produto, nome, preco, quantidade in cursor.fetchall():
    catalogo.append((id_produto, nome, preco))
    estoque[id_produto] = quantidade


# ===== Função: Cadastrar produtos =====
def cadastrar_produtos():
    print("\n--- Cadastro de Produtos ---")
    while True:
        continuar = input("Deseja cadastrar um produto? (sim/não): ").strip().lower()
        if continuar not in ['sim', 's', 'yes', 'y']:
            break

        # ID
        while True:
            try:
                id_produto = int(input("Digite o ID: "))
                if id_produto < 0:
                    print("ID não pode ser negativo.")
                    continue
                if any(produto[0] == id_produto for produto in catalogo):
                    print("ID já cadastrado, escolha outro.")
                    continue
            except ValueError:
                print("Digite um número inteiro.")
                continue
            break

        # Nome
        nome_produto = input("Digite o nome do produto: ").strip().lower()

        # Preço
        while True:
            try:
                preco_produto = float(input("Digite o preço do produto: "))
                if preco_produto < 0:
                    print("Preço não pode ser negativo.")
                    continue
            except ValueError:
                print("Digite um valor numérico.")
                continue
            break

        # Quantidade
        while True:
            try:
                qnt_produto = int(input("Digite a quantidade em estoque: "))
                if qnt_produto <= 0:
                    print("É necessário ter ao menos 1 unidade.")
                    continue
            except ValueError:
                print("Digite um número inteiro.")
                continue
            break

        # Adiciona ao catálogo e estoque
        catalogo.append((id_produto, nome_produto, preco_produto))
        estoque[id_produto] = qnt_produto

        # Adiciona ao banco
        cursor.execute(
            "INSERT INTO produtos (id, nome, preco, quantidade) VALUES (?, ?, ?, ?)",
            (id_produto, nome_produto, preco_produto, qnt_produto)
        )
        conexao.commit()
        print(f"Produto {nome_produto.capitalize()} cadastrado com sucesso!")


# ===== Função: Mostrar catálogo =====
def mostrar_catalogo():
    if not catalogo:
        print("Não há produtos no catálogo.")
        return
    print(f"{'ID':<5} {'Nome':<15} {'Preço':<10} {'Quantidade':<10}")
    print("-" * 45)
    for id_produto, nome, preco in catalogo:
        quantidade = estoque[id_produto]
        print(f"{id_produto:<5} {nome.capitalize():<15} R${preco:<10.2f} {quantidade:<10}")


# ===== Função: Aplicar desconto =====
def aplicar_desconto():
    print("\n--- Aplicar Desconto ---")
    while True:
        resposta = input("Deseja aplicar desconto a algum produto? (sim/não) ").strip().lower()
        if resposta in ['não', 'nao', 'n']:
            break
        elif resposta in ['sim', 's']:
            produto_id = int(input("Digite o ID do produto: "))
            desconto = float(input("Digite a porcentagem de desconto: "))

            for i, item in enumerate(catalogo):
                if item[0] == produto_id:
                    id_produto, nome, preco = item
                    novo_preco = preco * (1 - desconto / 100)

                    # Atualiza banco
                    cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?", (novo_preco, id_produto))
                    conexao.commit()

                    # Atualiza lista em memória
                    catalogo[i] = (id_produto, nome, novo_preco)

                    print(f"Novo preço aplicado: {id_produto:<5} {nome:<15} R${novo_preco:<10.2f}")
                    break
            else:
                print("ID não encontrado.")
        else:
            print("Resposta inválida.")


# ===== Função: Carrinho e Reposição =====
def gerenciar_carrinho():
    print("\n--- Carrinho / Reposição ---")
    carrinho = []

    while True:
        acao = input("Deseja adicionar ao carrinho ou repor estoque? (carrinho/repor/sair) ").strip().lower()

        if acao in ['sair', 'n', 'não', 'nao']:
            break

        elif acao in ['repor', 'atualizar']:
            id_repor = int(input("Digite o ID do produto a repor: "))
            if id_repor in estoque:
                qnt_repor = int(input("Digite a quantidade a repor: "))
                if qnt_repor <= 0:
                    print("Quantidade inválida.")
                    continue
                estoque[id_repor] += qnt_repor
                cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (estoque[id_repor], id_repor))
                conexao.commit()
                print(f"Estoque atualizado! Produto {id_repor} agora tem {estoque[id_repor]} unidades.")
            else:
                print("ID não encontrado no catálogo.")

        elif acao in ['carrinho', 'compra', 'adicionar']:
            add_prod = int(input("Digite o ID do produto desejado: "))
            if add_prod not in estoque:
                print("Produto não existe.")
                continue
            qnt_prod = int(input("Digite a quantidade desejada: "))
            if qnt_prod > estoque[add_prod]:
                print("Estoque insuficiente.")
                continue

            # Atualiza estoque
            estoque[add_prod] -= qnt_prod
            for item in catalogo:
                if item[0] == add_prod:
                    id_prod, nome_prod, preco_prod = item
                    break
            carrinho.append((id_prod, nome_prod, preco_prod, qnt_prod))
            cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (estoque[id_prod], id_prod))
            conexao.commit()
            print(f"{nome_prod.capitalize()} adicionado ao carrinho.")

        else:
            print("Opção inválida. Digite 'carrinho', 'repor' ou 'sair'.")

    return carrinho


# ===== Função: Mostrar carrinho =====
def mostrar_carrinho(carrinho):
    print("\n--- Carrinho ---")
    if not carrinho:
        print("Carrinho vazio.")
        return
    preco_total = 0
    for id_prod, nome, preco, qtd in carrinho:
        print(f"ID: {id_prod}, Nome: {nome.capitalize()}, Quantidade: {qtd}, Preço unitário: R${preco:.2f}")
        preco_total += preco * qtd
    print(f"Total a pagar: R${preco_total:.2f}")


# ===== Loop principal do sistema =====
def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar produto")
        print("2 - Dar desconto")
        print("3 - Carrinho / Reposição")
        print("4 - Mostrar catálogo")
        print("5 - Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            cadastrar_produtos()
        elif escolha == "2":
            aplicar_desconto()
        elif escolha == "3":
            carrinho = gerenciar_carrinho()
            mostrar_carrinho(carrinho)
        elif escolha == "4":
            mostrar_catalogo()
        elif escolha == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

# ===== Executa o sistema =====
menu_principal()