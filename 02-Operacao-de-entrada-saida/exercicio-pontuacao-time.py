"""
Faça um programa que peça o nome de um time de futebol,
a quantidade de vitórias e empates.
Sabendo que cada vitória vale 3 pontos e cada empate vale 1 ponto,
calcule e mostre a pontuação total do time.
"""

# Entrada de dados
time = input("Digite o nome de um time de futebol: ")
vit = int(input("Digite a quantidade de vitórias: "))
emp = int(input("Digite a quantidade de empates: "))

# Processamento computacional
pontos_total = (vit * 3) + emp

# Saída de informação
print(f"\n{time} possuí {vit} vitória(s) e {emp} empate(s), com um total de {pontos_total} pontos")