import pandas as pd

# Importação do arquivo CSV
jogos = pd.read_csv("intro_pandas/video_games.csv")
print(jogos, "\n")

# Tipo de dados de cada coluna
print(jogos.dtypes, "\n") 
print(jogos.info(), "\n")

# Leitura de valores de uma coluna em específico
jogos_name = jogos["name"]
print(jogos_name, "\n")

# Valor máximo de uma coluna
jogos["user_review"] = pd.to_numeric(jogos["user_review"], errors = "coerce") # Conversão coluna object em tipo numérico
jogos_review = jogos["user_review"].max()
print("Valor máximo da coluna de review de usuários: ", jogos_review, "\n")

# Dados de uma coluna com um determinado valor
jogo = jogos[jogos["name"] == "Metal Gear Solid"]
print(jogo, "\n")

jogo = jogos[jogos["name"].str.contains("Metal Gear Solid")]
print(jogo)