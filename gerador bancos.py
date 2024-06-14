import random


palavras = ["Bancos A", "Bancos B", "Bancos C", "Bancos D", "Bancos E"]


linhas = [random.choice(palavras) for _ in range(100)]


for linha in linhas:
    print(linha)
