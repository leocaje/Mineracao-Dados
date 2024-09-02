import pandas as pd

# Importação do arquivo
filmes = pd.read_csv("pandas_movies/tmdb_5000_credits.csv")

# Leitura do arquivo utilizando head
print(filmes.head(), "\n")

# Retorno das colunas da tabela
print(filmes.keys(), "\n")

# Dados das colunas "title" e "cast"
print(filmes.title.head(), "\n")
print(filmes.cast.head(), "\n")

# ----- DESAFIO -----

# Função para encontrar filmes do ator
def filmografia_ator(filmes, ator):
    # Lista para armazenar a filmografia do ator
    filmografia = []
    
    # Itera sobre as linhas do arquivo CSV
    for _, row in filmes.iterrows():
        elenco = row["cast"]  # Busca o conteúdo da coluna "cast"
        
        # Verifica se ator está na coluna "cast"
        if ator in elenco:
            filmografia.append(row["title"])  # Adiciona o filme à lista
    
    return filmografia

# Definição do ator
ator = "Chris Evans"
filmes = filmografia_ator(filmes, ator)

print(f"Filmes com {ator}:")
for filme in filmes:
    print(filme, " | ", ator)
