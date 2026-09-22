# Enunciado:

# Cria um programa que peça ao utilizador a idade e, depois, permita escolher filmes.

# O programa deve continuar a pedir o nome de um filme enquanto o utilizador não escrever sair.

# Para cada filme, o programa deve perguntar a classificação etária:

# L → Livre
# 10 → maiores de 10 anos
# 12 → maiores de 12 anos
# 16 → maiores de 16 anos
# 18 → maiores de 18 anos

# Utiliza if para verificar se o utilizador pode assistir ao filme.

# Quando escrever sair, o programa termina.
# ---------------------------------------------
# Exemplo:

# Qual é a sua idade? 15

# Digite o nome do filme: Homem-Aranha
# Classificação do filme: 12
# Você pode assistir!

# Digite o nome do filme: Filme de Terror
# Classificação do filme: 18
# Você não pode assistir!

# Digite o nome do filme: sair

# Programa encerrado!

idade = int(input("Digite a sua idade: "))

filme = input("\nDigite o nome do filme (ou digite 'sair' para finalizar): ")

while filme != "sair":
    classFilme = int(input("Classificação do filme: "))

    if classFilme <= idade:
        print("Você pode assistir!")
    else:
        print("Você não pode assistir!")

    filme = input("\nDigite o nome do filme (ou digite 'sair' para finalizar): ")

print("\nPrograma encerrado!")