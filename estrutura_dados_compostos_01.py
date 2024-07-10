# Lista contendo os nomes dos alunos e suas respectivas notas
notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

# Lista para armazenar apenas os nomes dos alunos
nomes = []
# Lista para armazenar todas as notas juntas
notas_juntas = []

# Loop para iterar sobre a lista 'notas_turma'
for i in range(len(notas_turma)):
  # Verifica se o índice é múltiplo de 4 (indicando que é um nome)
  if i % 4 == 0:
    # Adiciona o nome à lista 'nomes'
    nomes.append(notas_turma[i])
  else:
    # Adiciona a nota à lista 'notas_juntas'
    notas_juntas.append(notas_turma[i]) 

# Imprime a lista de nomes
print(nomes)

# Imprime a lista de notas juntas
print(notas_juntas)

# Lista para armazenar as notas separadas em sublistas (uma sublista para cada aluno)
notas = []

# Loop para iterar sobre a lista 'notas_juntas' de 3 em 3 elementos
for i in range(0, len(notas_juntas), 3):
  # Adiciona uma sublista de 3 notas à lista 'notas'
  notas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]])

# Imprime a primeira sublista de notas
print(notas[0])
# Imprime a terceira nota da primeira sublista de notas
print(notas[0][2])
