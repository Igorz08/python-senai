# Tupla contendo outras tuplas
alunos = (
    ("Carlos", 17),
    ("Ana", 18),
    ("João", 16)
)

# Acessando a primeira tupla
print(alunos[0])

# Carlos
print(alunos[0][0])

# idade do carlos
print(alunos[0][1])

# Percorrendo os alunos
for aluno in alunos:
    print("Nome:", aluno[0])
    print("Idade:", aluno[1])
    print("---------------------")