# Faça um programa em Python que peça o peso (kg) 
# e a altura (m) de um indivíduo. Calcule o IMC
# mostre a sua classificação:

# Menor que 18,5: abaixo do peso
# De 18,5 a 24,9: peso normal
# 25 ou mais: acima do peso

# peso / (altura ** 2)

# Solicitação de dados
peso = float(input("Insira a sua massa (kg): "))
altura = float(input("Insira a sua altura (m): "))

# Procedimento computacional
imc = peso / (altura ** 2)

# Resultados
print(f"\nSeu IMC é: {imc:.2f}\n")

# Classificação
if imc <= 18.5:
    print("Você está abaixo do peso")
elif imc <= 24.9:
    print("Você está com o peso normal")
else:
    print("Você está acima do peso")