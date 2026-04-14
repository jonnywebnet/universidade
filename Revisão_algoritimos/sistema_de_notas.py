# cria uma lista vazia para armazenar os alunos
alunos = []

def adicionar_aluno():
    # pede o nome do aluno
    nome = input("Nome do aluno: ")

    # lista para guardar as notas
    notas = []

    # loop para garantir quantidade válida de notas
    while True:
        try:
            # tenta converter a entrada para inteiro
            qtd = int(input("Quantas notas? (2 a 5): "))
            
            # verifica se está no intervalo permitido
            if 2 <= qtd <= 5:
                break  # sai do loop se estiver correto
            else:
                print("Digite entre 2 e 5 notas.")
        except:
            # caso o usuário digite algo inválido
            print("Valor inválido.")

    # loop para ler cada nota
    for i in range(qtd):
        while True:
            try:
                # tenta ler a nota como número decimal
                nota = float(input(f"Nota {i+1}: "))
                
                # valida se está entre 0 e 10
                if 0 <= nota <= 10:
                    notas.append(nota)  # adiciona na lista
                    break
                else:
                    print("Nota deve ser entre 0 e 10.")
            except:
                print("Valor inválido.")

    # calcula a média
    media = sum(notas) / len(notas)

    # cria o dicionário do aluno
    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media
    }

    # adiciona o aluno na lista principal
    alunos.append(aluno)


def ordenar_alunos():
    # retorna uma nova lista ordenada pela média (maior → menor)
    return sorted(alunos, key=lambda x: x["media"], reverse=True)


def salvar_em_arquivo():
    try:
        # abre o arquivo no modo escrita ("w" apaga o conteúdo anterior)
        with open("alunos.txt", "w") as f:
            # percorre todos os alunos
            for aluno in alunos:
                # escreve nome e média separados por vírgula
                f.write(f"{aluno['nome']},{aluno['media']}\n")
        print("Dados salvos com sucesso.")
    except:
        # caso dê erro (permissão, etc)
        print("Erro ao salvar arquivo.")


# adiciona 2 alunos (exemplo)
for _ in range(2):
    adicionar_aluno()

# ordena os alunos
ordenados = ordenar_alunos()

print("\nAlunos ordenados:")
# mostra os alunos ordenados
for a in ordenados:
    print(f"{a['nome']} - Média: {a['media']:.2f}")

# salva no arquivo
salvar_em_arquivo()