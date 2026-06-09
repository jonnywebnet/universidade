import random
import time

def counting(lista, exp):

    n = len(lista)

    saida = [0] * n

    contagem = [0] * 10

    for i in range(n):
        indice = lista[i] // exp
        contagem[indice % 10] += 1

    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    i = n - 1

    while i >= 0:
        indice = lista[i] // exp
        saida[contagem[indice % 10] - 1] = lista[i]
        contagem[indice % 10] -= 1
        i -= 1

    for i in range(n):
        lista[i] = saida[i]

def radix_sort(lista):

    maior = max(lista)

    exp = 1

    while maior // exp > 0:
        counting(lista, exp)
        exp *= 10

    return lista

lista = [random.randint(0, 1000000) for _ in range(100000)]

print(lista[:10])

inicio = time.perf_counter()
radix_sort(lista)
fim = time.perf_counter()

print(lista[:10])
print(f"{fim - inicio:.6f} segundos")
