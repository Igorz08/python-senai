# Faça um programa em Python que peça a nota de um aluno 
# e verifique se ele foi aprovado ou reprovado.

# Nota maior ou igual a 6 → Aprovado
# Nota menor que 6 → Reprovado

# Solicita a nota
nota = float(input("Digite sua nota: "))

# Verifica se foi aprovavdo
if nota >= 6:
    print("\nAprovado")
else:
    print("\nReprovado")
