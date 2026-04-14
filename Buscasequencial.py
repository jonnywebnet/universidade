import random
import time

inicio = time.time()
lista= []

for i in range(1000000000):
    a = random.randint(0,500)
    lista.append(a)

print(lista)
final = time.time()

tempo = final-inicio
print(f"{tempo:.2f}")
