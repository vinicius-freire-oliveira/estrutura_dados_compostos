# Lista contendo os nomes dos estudantes
estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]

# Imprime a lista de estudantes
print(estudantes)

# Importa a função randint do módulo random
from random import randint

# Define uma função que gera um código aleatório de 3 dígitos
def gera_codigo():
  # Gera um número aleatório entre 0 e 999 e o converte para string
  return str(randint(0, 999))

# Lista para armazenar os estudantes e seus códigos
codigo_estudantes = []

# Loop para iterar sobre a lista 'estudantes'
for i in range(len(estudantes)):
  # Adiciona à lista 'codigo_estudantes' uma tupla contendo o nome do estudante e um código
  # O código é composto pela primeira letra do nome do estudante concatenada com o código aleatório gerado
  codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))

# Imprime a lista de estudantes com seus respectivos códigos
print(codigo_estudantes)


