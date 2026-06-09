import random
import time


def counting_sort(lista):

    maior = max(lista)

    contagem = [0] * (maior + 1)

    for numero in lista:
        contagem[numero] += 1

    resultado = []

    for i in range(len(contagem)):
        resultado.extend([i] * contagem[i])

    return resultado


lista = [random.randint(0, 1000000) for _ in range(100000)]

print(lista[:10])

inicio = time.perf_counter()
lista = counting_sort(lista)
fim = time.perf_counter()

print(lista[:10])
print(f"{fim - inicio:.6f} segundos")
