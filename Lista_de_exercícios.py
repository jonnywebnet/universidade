Verde = "\033[92m"
Reset = "\033[0m"

print(Verde + "Exercício 1:" + Reset)
print("Olá, mundo!")
print()

print(Verde + "Exercício 2:" + Reset)
numero = int(input("Digite um número inteiro: "))
atecessor = numero - 1
sucessor = numero + 1
print(f"Você digitou: {numero}")
print(f"O antecessor de {numero} é {atecessor}")
print(f"O sucessor de {numero} é {sucessor}")
print()

print(Verde + "Exercício 3:" + Reset)
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
soma = numero1 + numero2
print(f"A soma dos números {numero1} e {numero2} é {soma}")
print()

print(Verde + "Exercício 4:" + Reset)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas {nota1}, {nota2} e {nota3} é {media:.2f}")
print()

print(Verde + "Exercício 5:" + Reset)
metros = float(input("Digite a distância em metros: "))
centimetros = metros * 100
print(f"{metros} metros equivalem a {centimetros} centímetros.")
print()

print(Verde + "Exercício 6:" + Reset)
numero_tauada = int(input("Digite um número inteiro para ver sua tabuada: "))
print(f"Tabuada do {numero_tauada}:")
for i in range(1, 11):
    resultado = numero_tauada * i
    print(f"{numero_tauada} x {i} = {resultado}")
print()

print(Verde + "Exercício 7:" + Reset)
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F.")  
print()

print(Verde + "Exercício 8:" + Reset)
area = float(input("Digite o valor da base do retângulo: "))
altura = float(input("Digite o valor da altura do retângulo: "))
area_retangulo = area * altura
print(f"A área do retângulo é: {area_retangulo:.2f}")
print()

print(Verde + "Exercício 9:" + Reset)
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
print()

print(Verde + "Exercício 10:" + Reset)
numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print("O número é zero.")
print()

print(Verde + "Exercício 11:" + Reset)
altura = float(input("Digite sua altura em metros (ex: 1.60): "))
peso = float(input("Digite seu peso em kg: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")
print()

print(Verde + "Exercício 12:" + Reset)
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
maior = max(n1, n2, n3)
print(f"O maior número é {maior}")
print()

print(Verde + "Exercício 13:" + Reset)
numero = int(input("Digite um número: "))
if numero % 3 == 0:
    print(f"{numero} é múltiplo de 3")
else:
    print(f"{numero} não é múltiplo de 3")
print()

print(Verde + "Exercício 14:" + Reset)
numero = int(input("Digite um número inteiro positivo: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero} é {fatorial}")


#numero = int(input("Digite um número inteiro positivo: "))
#if numero < 0:
#    print("Fatorial não definido para números negativos!")
#elif numero == 0:
#    print("0! = 1")
#else:
#    fatorial = 1
#    print(f"Cálculo de {numero}!:")
#    for i in range(numero, 0, -1):
#        print(f"{fatorial} x {i} = ", end="")
#        fatorial *= i
#        print(fatorial)
#    print(f"Resultado final: {fatorial}")

print()

print(Verde + "Exercício 15:" + Reset)
a, b = 0, 1
print("10 primeiros números de Fibonacci:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()
print()

print(Verde + "Exercício 16:" + Reset)
for i in range(1, 101):
    print(i, end=" ")
print()
print()

print(Verde + "Exercício 17:" + Reset)
n = int(input("Digite um número N: "))
soma = sum(range(1, n + 1))
print(f"A soma de 1 até {n} é {soma}")
print()

'''
resolução da aula:
n = 5
fat = 1
for i in range(1,n+1):
    fat *= i
print(fat) 
'''
print(Verde + "Exercício 18:" + Reset)
soma = 0
while True:
    num = float(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    soma += num
print(f"A soma total é {soma}")
print()

print(Verde + "Exercício 19:" + Reset)
pares = 0
for i in range(1, 51):
    if i % 2 == 0:
        pares += 1
print(f"Existem {pares} números pares entre 1 e 50")
print()

print(Verde + "Exercício 20:" + Reset)
numero = int(input("Digite um número inteiro: "))
invertido = int(str(numero)[::-1])
print(f"O número invertido é {invertido}")
print()

print(Verde + "Exercício 21:" + Reset)
palavra = input("Digite uma palavra: ").lower()
if palavra == palavra[::-1]:
    print(f"{palavra} é um palíndromo")
else:
    print(f"{palavra} não é um palíndromo")
print()

print(Verde + "Exercício 22:" + Reset)
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contagem = sum(1 for letra in frase if letra in vogais)
print(f"A frase tem {contagem} vogais")
print()

print(Verde + "Exercício 23:" + Reset)
frase = input("Digite uma frase: ")
nova_frase = frase.replace(" ", "-")
print(f"Frase com hifens: {nova_frase}")
print()

print(Verde + "Exercício 24:" + Reset)
numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para parar): ")
    if entrada.lower() == 'fim':
        break
    numeros.append(float(entrada))
if numeros:
    print(f"Maior: {max(numeros)} | Menor: {min(numeros)}")
else:
    print("Nenhum número digitado")
print()

print(Verde + "Exercício 25:" + Reset)
numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para parar): ")
    if entrada.lower() == 'fim':
        break
    numeros.append(float(entrada))
numeros.sort()
print("Lista ordenada:", numeros)
print()

print(Verde + "Exercício 26:" + Reset)
numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para parar): ")
    if entrada.lower() == 'fim':
        break
    numeros.append(float(entrada))
unicos = list(set(numeros))
print("Lista sem duplicatas:", unicos)
print()

print(Verde + "Exercício 27:" + Reset)
numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para parar): ")
    if entrada.lower() == 'fim':
        break
    numeros.append(float(entrada))
print(f"Soma dos elementos: {sum(numeros)}")
print()

print(Verde + "Exercício 28:" + Reset)
numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para parar): ")
    if entrada.lower() == 'fim':
        break
    numeros.append(float(entrada))
alvo = float(input("Digite o número que quer contar: "))
contagem = numeros.count(alvo)
print(f"O número {alvo} aparece {contagem} vezes")
print()

print(Verde + "Exercício 29:" + Reset)
pessoas = {}
while True:
    nome = input("Digite o nome (ou 'fim' para parar): ")
    if nome.lower() == 'fim':
        break
    idade = int(input(f"Digite a idade de {nome}: "))
    pessoas[nome] = idade
print("Dados cadastrados:")
for nome, idade in pessoas.items():
    print(f"{nome}: {idade} anos")
print()

print(Verde + "Exercício 30:" + Reset)
pessoas = {}
pessoas["João"] = 10
pessoas["Maria"] = 12
print("Pontuação dos participantes:", pessoas)
pessoas["João"] = int(input("Digite a nova pontuação de João: ")) 
pessoas["Maria"] = int(input("Digite a nova pontuação de Maria: "))
print("Nova pontuação dos participantes:", pessoas)
print()

print(Verde + "Exercício 31:" + Reset)
def soma(a, b):
    return a + b
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print(f"A soma é {soma(n1, n2)}")
print()

print(Verde + "Exercício 32:" + Reset)
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
numero = int(input("Digite um número: "))
if eh_primo(numero):
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")
print()

print(Verde + "Exercício 33:" + Reset)
import math
def area_circulo(raio):
    return math.pi * raio ** 2
raio = float(input("Digite o raio do círculo: "))
print(f"A área do círculo é ~{area_circulo(raio):.2f}")
print()

print(Verde + "Exercício 34:" + Reset)
def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)
numero = int(input("Digite um número: "))
print(f"Fatorial de {numero} = {fatorial_recursivo(numero)}")
print()

print(Verde + "Exercício 35:" + Reset)
quadrados = [x**2 for x in range(1, 11)]
print("Quadrados de 1 a 10:", quadrados)
print()

print(Verde + "Exercício 36:" + Reset)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print("Números pares:", pares)
print()

print(Verde + "Exercício 37:" + Reset)
nome_arquivo = input("Digite o nome do arquivo de texto (ex: texto.txt): ")
try:
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    print(f"O arquivo tem {len(linhas)} linhas")
except FileNotFoundError:
    print("Arquivo não encontrado")
print()

print(Verde + "Exercício 38:" + Reset)
nome_arquivo = "saida.txt"
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write("Olá, este é um teste!\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
print(f"Dados escritos no arquivo {nome_arquivo}")
print()

print(Verde + "Exercício 39:" + Reset)
while True:
    print("\nMenu:")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        print("Saindo...")
        break
    elif opcao == "1":
        print("Você escolheu a opção 1")
    elif opcao == "2":
        print("Você escolheu a opção 2")
    else:
        print("Opção inválida")
print()

print(Verde + "Exercício 40:" + Reset)
try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida")
except ValueError:
    print("Erro: Digite números válidos")
print()