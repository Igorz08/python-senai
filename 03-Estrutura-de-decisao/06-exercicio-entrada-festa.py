# 18 anos ou mais: Pode entrar na festa.
# 16 ou 17 anos: Pode entrar com responsável.
# Menos de 16 anos: Não pode entrar na festa.

# Entrada de dados
idade = int(input("Digite sua idade: "))

# Verifica a idade
if idade >= 18:
    print("\nVocê pode entrar na festa")
elif idade == 16 or idade == 17:
    print("\nVocê só pode entrar na festa com responsável")
else:
    print("\nVocê não pode entrar na festa")