# Programa: Verificação de passagem

# Faça um programa em Python que peça a idade de uma pessoa
# e verifique se ela paga passagem inteira ou meia passagem.

# Idade menor ou igual a 12 → Meia passagem
# Idade maior que 12 → Passagem inteira

# Solicita a idade
idade = int(input("Digite sua idade: "))

# Verifica a idade
if idade <= 12:
    print("\nVocê pagará meia passagem")
else:
    print("\nVocê pagará a passagem inteira")