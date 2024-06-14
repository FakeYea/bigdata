import random


numeros = [random.randint(500, 5000) for _ in range(100)]


for numero in numeros:
    print(numero)
