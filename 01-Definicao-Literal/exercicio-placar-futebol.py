# Objetivo:
# Praticar variáveis, números inteiros, operações matemáticas e f-strings.

# Descrição:
# Crie um programa que represente o resultado de uma partida de futebol.
#  O programa deve armazenar o nome de dois times 
#  e a quantidade de golos marcados por cada equipa.

# Depois, apresente o placar e calcule o total de golos da partida.

# Resultado no terminal
# ================================
#         RESULTADO DO JOGO
# ================================
# França 3 x 2 Espanha
# Total de golos: 5
# ================================

time1 = "Franca"
time2 = "Espanha"
GolsTime1 = 3
GolsTime2 = 2
GolsTotal = GolsTime1 + GolsTime2

print("================================")
print("        RESULTADO DO JOGO")
print("================================")
print(f"{time1} {GolsTime1} x {GolsTime2} {time2}")
print(f"Total de gols: {GolsTotal}")
print("================================")