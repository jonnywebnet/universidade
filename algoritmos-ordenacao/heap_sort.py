import random
import time
import heapq


def heap_sort(lista):

    heapq.heapify(lista)

    ordenada = []

    while lista:
        ordenada.append(heapq.heappop(lista))

    return ordenada


lista = [random.randint(0, 1000000) for _ in range(100000)]

print(lista[:10])

inicio = time.perf_counter()
lista = heap_sort(lista)
fim = time.perf_counter()

print(lista[:10])
print(f"{fim - inicio:.6f} segundos")
