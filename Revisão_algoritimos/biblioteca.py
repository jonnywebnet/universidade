import os  # usado para verificar se o arquivo existe

# lista de livros
livros = []

def adicionar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")

    # valida o ano
    while True:
        try:
            ano = int(input("Ano: "))
            if ano > 0:
                break
            else:
                print("Ano inválido.")
        except:
            print("Valor inválido.")

    # valida número de páginas
    while True:
        try:
            paginas = int(input("Páginas: "))
            if paginas > 0:
                break
            else:
                print("Número inválido.")
        except:
            print("Valor inválido.")

    # adiciona o livro na lista
    livros.append({
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "paginas": paginas
    })


def listar_livros():
    # percorre e imprime todos os livros
    for l in livros:
        print(l)


def ordenar_livros():
    # usuário escolhe o campo
    campo = input("Ordenar por (ano/paginas): ")
    
    # usuário escolhe a ordem
    ordem = input("Ordem (crescente/decrescente): ")

    # define se será reverso ou não
    reverse = True if ordem == "decrescente" else False

    # ordena a lista
    livros.sort(key=lambda x: x[campo], reverse=reverse)


def salvar_livros():
    try:
        # abre arquivo para escrita
        with open("biblioteca.txt", "w") as f:
            for l in livros:
                # salva cada livro em uma linha
                f.write(f"{l['titulo']},{l['autor']},{l['ano']},{l['paginas']}\n")
        print("Salvo com sucesso.")
    except:
        print("Erro ao salvar.")


def carregar_livros():
    # verifica se o arquivo existe
    if not os.path.exists("biblioteca.txt"):
        print("Arquivo não existe.")
        return

    try:
        with open("biblioteca.txt", "r") as f:
            for linha in f:
                # divide a linha pelos dados separados por vírgula
                titulo, autor, ano, paginas = linha.strip().split(",")

                # adiciona na lista convertendo tipos
                livros.append({
                    "titulo": titulo,
                    "autor": autor,
                    "ano": int(ano),
                    "paginas": int(paginas)
                })
        print("Dados carregados.")
    except:
        print("Erro ao carregar.")


# menu principal
while True:
    print("\n1-Adicionar\n2-Listar\n3-Ordenar\n4-Salvar\n5-Carregar\n6-Sair")
    op = input("> ")

    if op == "1":
        adicionar_livro()
    elif op == "2":
        listar_livros()
    elif op == "3":
        ordenar_livros()
    elif op == "4":
        salvar_livros()
    elif op == "5":
        carregar_livros()
    elif op == "6":
        break  # encerra o programa