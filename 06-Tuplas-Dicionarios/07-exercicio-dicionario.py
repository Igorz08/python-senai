# Enunciado:
# Crie um dicionário com 5 alunos e suas respectivas idades. 
# Use for para percorrer o dicionário e if para mostrar apenas 
# os alunos com idade maior ou igual a 18 anos.

# Saída:

# Ana é maior de idade: 20
# Mariana é maior de idade: 19
# Pedro é maior de idade: 18

# Dicionário com alunos e suas idades
alunos = {
    "Carlos": 17,
    "Ana": 20,
    "João": 16,
    "Mariana": 19,
    "Pedro": 18
}

for aluno in alunos:
    if aluno[1] >= 18:
        print(f"{aluno[0]} é maior de idade: {aluno[1]}")