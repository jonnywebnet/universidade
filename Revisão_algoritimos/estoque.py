import os  # usado para verificar arquivos

# lista de produtos
produtos = []

def adicionar_produto():
    nome = input("Nome: ")
    categoria = input("Categoria: ")

    # valida preço
    while True:
        try:
            preco = float(input("Preço: "))
            if preco > 0:
                break
            else:
                print("Preço inválido.")
        except:
            print("Valor inválido.")

    # valida quantidade
    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade >= 0:
                break
            else:
                print("Quantidade inválida.")
        except:
            print("Valor inválido.")

    # adiciona produto
    produtos.append({
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    })


def atualizar_quantidade():
    nome = input("Nome do produto: ")

    # procura o produto na lista
    for p in produtos:
        if p["nome"] == nome:
            try:
                # valor pode ser positivo ou negativo
                valor = int(input("Quantidade a alterar (+/-): "))
                p["quantidade"] += valor  # atualiza quantidade
                print("Atualizado.")
            except:
                print("Valor inválido.")
            return

    print("Produto não encontrado.")


def listar_produtos():
    for p in produtos:
        print(p)


def ordenar_produtos():
    campo = input("Ordenar por (preco/quantidade): ")
    ordem = input("Ordem (crescente/decrescente): ")

    reverse = True if ordem == "decrescente" else False

    # ordena lista
    produtos.sort(key=lambda x: x[campo], reverse=reverse)


def salvar_estoque():
    try:
        with open("estoque.txt", "w") as f:
            for p in produtos:
                f.write(f"{p['nome']},{p['categoria']},{p['preco']},{p['quantidade']}\n")
        print("Salvo com sucesso.")
    except:
        print("Erro ao salvar.")


def carregar_estoque():
    if not os.path.exists("estoque.txt"):
        print("Arquivo não existe.")
        return

    try:
        with open("estoque.txt", "r") as f:
            for linha in f:
                nome, categoria, preco, quantidade = linha.strip().split(",")

                produtos.append({
                    "nome": nome,
                    "categoria": categoria,
                    "preco": float(preco),
                    "quantidade": int(quantidade)
                })
        print("Dados carregados.")
    except:
        print("Erro ao carregar.")


# menu
while True:
    print("\n1-Adicionar\n2-Atualizar\n3-Listar\n4-Ordenar\n5-Salvar\n6-Carregar\n7-Sair")
    op = input("> ")

    if op == "1":
        adicionar_produto()
    elif op == "2":
        atualizar_quantidade()
    elif op == "3":
        listar_produtos()
    elif op == "4":
        ordenar_produtos()
    elif op == "5":
        salvar_estoque()
    elif op == "6":
        carregar_estoque()
    elif op == "7":
        break