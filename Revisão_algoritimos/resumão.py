#⚡ RESUMÃO FINAL — ALGORITMOS (PROVA)
#🧠 1. Estrutura principal (CAI EM TODAS)
lista = []

item = {
    "campo1": valor,
    "campo2": valor
}

lista.append(item)

#👉 Sempre é lista de dicionários

#🔢 2. Entrada + validação (ESSENCIAL)
while True:
    try:
        valor = int(input("Digite: "))
        if valor > 0:
            break
        else:
            print("Inválido")
    except:
        print("Erro")

#👉 Cai pra:

nota (0–10)
ano (>0)
páginas (>0)
quantidade (>=0)
preço (>0)
#📊 3. Média (Questão 1)
media = sum(notas) / len(notas)
#🔄 4. Ordenação (MUITO IMPORTANTE)
lista.sort(key=lambda x: x["campo"], reverse=True)

#ou

ordenado = sorted(lista, key=lambda x: x["campo"], reverse=True)

#👉 exemplos:

"media"
"ano"
"paginas"
"preco"
"quantidade"
#💾 5. Salvar arquivo
with open("arquivo.txt", "w") as f:
    for item in lista:
        f.write(f"{item['campo1']},{item['campo2']}\n")
📂 6. Ler arquivo
with open("arquivo.txt", "r") as f:
    for linha in f:
        dados = linha.strip().split(",")

#👉 depois monta o dicionário:

{
    "nome": dados[0],
    "valor": int(dados[1])
}
#⚠️ 7. Tratar erro de arquivo
try:
    with open("arquivo.txt", "w") as f:
        pass
except:
    print("Erro ao salvar")
#📁 8. Verificar se arquivo existe
import os

if os.path.exists("arquivo.txt"):
#📋 9. Menu (Questão 2 e 3)
while True:
    print("1-Opção\n2-Sair")
    op = input("> ")

    if op == "1":
        pass
    elif op == "2":
        break
#🔁 10. Percorrer lista
for item in lista:
    print(item)
#🧩 COMO MONTAR QUALQUER QUESTÃO (PASSO A PASSO)
#cia lista
#cria função adicionar
#valida dados com try
#usa dicionário
#append na lista
#cria ordenar (lambda)
#cria salvar (write)
#cria carregar (split)
#menu

#👉 ISSO resolve as 3 questões

#🚀 TRUQUE PRA PROVA

#Se travar:

#👉 escreve primeiro:

lista = []

#👉 depois:

#def adicionar():

#👉 depois:

#lista.append({...})

#👉 depois:

#lista.sort(key=lambda x: x["campo"])

#👉 depois arquivo

#💥 pronto, já fez 70% da questão

#⚠️ ERROS QUE MAIS REPROVAM
#esquecer append()
#esquecer lambda
#não usar try/except
#não converter int() / float()
#errar split(",")
#🔥 ÚLTIMA DICA (sério)

#Não tenta decorar código.

#👉 decora só isso:
#lista + dicionário
#sort com lambda
#open/write/read
#try/except