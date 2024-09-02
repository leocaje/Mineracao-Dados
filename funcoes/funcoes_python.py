def saudacao():
  print("Olá, mundo!")
        
# Chamando função
saudacao()

def saudacao_personalizada(nome):
  print("Olá, ", nome + "!")

saudacao_personalizada("Léo")

def soma(a, b):
  resultado = a + b
  return resultado 

total = soma(3, 5)
print(total)
