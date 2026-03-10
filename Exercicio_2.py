print("Exercicio da aula 2")

Vermelho  = "\033[31m"
Verde     = "\033[92m"
Amarelo   = "\033[33m"
Reset = "\033[0m"

print(Verde + "PARTE 1:" + Reset)
print()

print(Verde + "Exercício 1:" + Reset)
frutas = ["maçã", "banana", "laranja"]
print(frutas[1])
print()

print(Verde + "Exercício 2:" + Reset)
frutas.append("uva")
frutas.remove("banana")
print(frutas)
print()

print(Verde + "Exercício 3:" + Reset)
numeros = []
for i in range(1, 11):
    numeros.append(i)
    print(len(numeros))
print()

print(Verde + "Exercício 4:" + Reset)
if 7 in numeros:
    print("Sim")
else:
    print("Não")
print()

print(Verde + "Exercício 5:" + Reset)
slicing = numeros[0:3]
print(slicing)
print()

print(Verde + "Exercício 6:" + Reset)
notas = [8.5, 7.0, 9.5, 6.0] 
notas.sort(reverse=True)
print(notas)
print()

print(Verde + "Exercício 7:" + Reset)
numeros = [1, 2 ,2, 3, 4, 2, 5]
print(f"lista atualizada: {numeros}")
numero = 2
contador = 0

for i in numeros:
    if i == numero:
        contador += 1

print(f"O número {numero} aparece {contador} vezes na lista.")
print()

print(Verde + "Exercício 8:" + Reset)
print("Números invertidos:")
numeros_invertidos = numeros[::-1]
print(numeros_invertidos)
print()

print(Verde + "Exercício 9:" + Reset)
quadrados = [x**2 for x in range(1,9)]
print(quadrados)
print() 

print(Verde + "Exercício 10:" + Reset)
palavras = ["python", "lista", "exercicio", "legal"]
palavras_filtradas = [p for p in palavras if len(p) >= 5]
print("Lista original:", palavras)
print("Palavras com 5 ou mais letras:", palavras_filtradas)

print(Verde + "Exercício 11:" + Reset)
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print()

print(Verde + "Exercício 12:" + Reset)
lista = [1, 2, 2, 3, 4, 4, 5]
sem_duplicados = []

for i in lista:
    if i not in sem_duplicados:
        sem_duplicados.append(i)

print("Lista sem duplicados:", sem_duplicados)
print()

print(Verde + "Exercício 13:" + Reset)
def maior_menor(lista):
    return max(lista), min(lista)

valores = [10, 3, 25, 7, 1]
maior, menor = maior_menor(valores)

print("Maior:", maior)
print("Menor:", menor)
print()

print(Verde + "Exercício 14:" + Reset)
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print("O elemento da linha 1, coluna 2 é:", matriz[0][1])
print()

print(Verde + "Exercício 15:" + Reset)
import copy

matriz = [[1,2],[3,4]]
copia = copy.deepcopy(matriz)

copia[0][0] = 99

print("Original:", matriz)
print("Cópia alterada:", copia)
print()

print(Verde + "Exercício 16:" + Reset)
pares = [x for x in range(1, 21) if x % 2 == 0]
print(pares)
print()

print(Verde + "Exercício 17:" + Reset)
def mesmas_listas(lista1, lista2):
    return sorted(lista1) == sorted(lista2)

l1 = [1,2,3]
l2 = [3,2,1]

print(mesmas_listas(l1, l2))
print()

print(Verde + "Exercício 18:" + Reset)
import random

numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
print("Lista original:", numeros_aleatorios)

pares = [x for x in numeros_aleatorios if x % 2 == 0]
pares.sort()

print("Pares ordenados:", pares)
print()

print(Verde + "Exercício 19:" + Reset)
numeros = [1,2,3,4,5,6,7,8]

for i in numeros[:]:
    if i < 5:
        numeros.remove(i)

print(numeros)
print()

print(Verde + "Exercício 20:" + Reset)
def soma_acumulada(lista):
    resultado = []
    soma = 0

    for i in lista:
        soma += i
        resultado.append(soma)

    return resultado

lista = [1,2,3]
print(soma_acumulada(lista))
print()

print(Verde + "PARTE 2:" + Reset)
print()

print(Verde + "Exercícios 2 - 1:" + Reset)
aluno = {
    "nome": "João",
    "idade": 18,
    "nota": 9.5
}

print(aluno["idade"])
print()


print(Verde + "Exercícios 2 - 2:" + Reset)
aluno["cidade"] = "São Paulo"

print("Chaves do dicionário:")
for chave in aluno:
    print(chave)
print()


print(Verde + "Exercícios 2 - 3:" + Reset)
for chave, valor in aluno.items():
    print(chave, ":", valor)
print()


print(Verde + "Exercícios 2 - 4:" + Reset)
estoque = {
    "maçã": 10,
    "banana": 5
}

if "laranja" not in estoque:
    estoque["laranja"] = 0

print(estoque)
print()


print(Verde + "Exercícios 2 - 5:" + Reset)

agenda = []

contato1 = {
    "nome": "Carlos",
    "telefone": "99999-1111",
    "email": "carlos@email.com"
}

contato2 = {
    "nome": "Ana",
    "telefone": "98888-2222",
    "email": "ana@email.com"
}

agenda.append(contato1)
agenda.append(contato2)

print("Telefone do primeiro contato:", agenda[0]["telefone"])
print()

print(Verde + "PARTE 3:" + Reset)
print()

print(Verde + "Exercício 3 - Lista de Tarefas" + Reset)

tarefas = []

while True:

    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")

        tarefa = {
            "nome": nome,
            "feito": False
        }

        tarefas.append(tarefa)


    elif opcao == "2":

        if len(tarefas) == 0:
            print(Vermelho + "Nenhuma tarefa cadastrada." + Reset)

        else:
            for i, tarefa in enumerate(tarefas):

                status = Verde + "FEITO" + Reset if tarefa["feito"] else Amarelo + "ESPERA" + Reset

                print(f"{i+1} - {tarefa['nome']} [{status}]")


    elif opcao == "3":

        try:
            numero = int(input("Número da tarefa: ")) - 1

            if 0 <= numero < len(tarefas):
                tarefas[numero]["feito"] = True
            else:
                print(Vermelho + "Tarefa inválida" + Reset)

        except:
            print(Amarelo + "Digite um número válido" + Reset)


    elif opcao == "4":

        try:
            numero = int(input("Número da tarefa para remover: ")) - 1

            if 0 <= numero < len(tarefas):
                tarefas.pop(numero)
            else:
                print(Vermelho + "Tarefa inválida" + Reset)

        except:
            print(Amarelo + "Digite um número válido" + Reset)


    elif opcao == "5":
        print(Amarelo + "Saindo..." + Reset)
        break

    else:
        print(Vermelho + "Opção inválida" + Reset)