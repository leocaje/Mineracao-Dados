import pandas as pd

"""
Criar um DataFrame com o nome frutas no seguinte formato:
  | Maça | Banana
0 |  30  |   20
"""
print("Exercício 1:\n")

qtde_frutas = {"Maçã": [30], "Banana": [20]}
frutas = pd.DataFrame(qtde_frutas)

print(frutas, "\n")

"""
Criar um DataFrame com o nome frutas no seguinte formato:
            | Maça | Banana
Vendas 2022 | 1000 |   700
Vendas 2023 | 5000 |  2000
"""
print("Exercício 2:\n")

qtde_frutas = {"Maçã": [1000, 5000], "Banana": [700, 2000]}
index = ["Vendas 2022", "Vendas 2023"]
frutas = pd.DataFrame(qtde_frutas, index = index)

print(frutas, "\n")