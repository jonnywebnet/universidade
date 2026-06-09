import random
import time

def quick_sort(lista):

    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]

    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)

lista = [random.randint(0, 1000000) for _ in range(100000)]

print(lista[:10])

inicio = time.perf_counter()
lista = quick_sort(lista)
fim = time.perf_counter()

print(lista[:10])
print(f"{fim - inicio:.6f} segundos")
