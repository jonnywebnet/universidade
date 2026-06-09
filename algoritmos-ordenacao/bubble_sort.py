import random
import time

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

lista = [random.randint(0, 1000000) for _ in range(100000)]

print(lista[:10])

inicio = time.perf_counter()
bubble_sort(lista)
fim = time.perf_counter()

print(lista[:10])
print(f"{fim - inicio:.6f} segundos")
