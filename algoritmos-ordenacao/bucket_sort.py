import random
import time

def insertion_sort(lista):

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista

def bucket_sort(lista):

    quantidade = 10

    buckets = [[] for _ in range(quantidade)]

    maior = max(lista)

    for numero in lista:
        indice = numero * quantidade // (maior + 1)
        buckets[indice].append(numero)

    resultado = []

    for bucket in buckets:
        insertion_sort(bucket)
        resultado.extend(bucket)

    return resultado

lista = [random.randint(0, 1000000) for _ in range(100000)]

print(lista[:10])

inicio = time.perf_counter()
lista = bucket_sort(lista)
fim = time.perf_counter()

print(lista[:10])
print(f"{fim - inicio:.6f} segundos")
