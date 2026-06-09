import random
import time

def merge_sort(lista):

    if len(lista) > 1:

        meio = len(lista) // 2

        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):

            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1

            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

    return lista

lista = [random.randint(0, 1000000) for _ in range(100000)]

print(lista[:10])

inicio = time.perf_counter()
merge_sort(lista)
fim = time.perf_counter()

print(lista[:10])
print(f"{fim - inicio:.6f} segundos")
