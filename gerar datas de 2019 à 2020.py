import random
from datetime import datetime, timedelta


def gerar_data_aleatoria(inicio, fim):
    delta = fim - inicio
    aleatorio_dias = random.randint(0, delta.days)
    return inicio + timedelta(days=aleatorio_dias)


data_inicio = datetime(2019, 1, 1)
data_fim = datetime(2020, 12, 31)


datas = [gerar_data_aleatoria(data_inicio, data_fim) for _ in range(100)]


for data in datas:
    print(data.strftime('%d/%m/%Y'))
