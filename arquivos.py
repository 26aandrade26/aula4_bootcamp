import csv

caminho_do_arquivo: str = "exemplo.csv"

arquivo_scv: list = []

with open(file=caminho_do_arquivo, mode="r", encoding='utf-8') as arquivo:
    leitor_scv = csv.DictReader(arquivo)

    for linha in leitor_scv:
        arquivo_scv.append(linha)


print(arquivo_scv)
