import random


palavras = ["Contas A", "Contas B", "Contas C", "Contas D", "Contas E"]


linhas = [random.choice(palavras) for _ in range(100)]


for linha in linhas:
    print(linha)
