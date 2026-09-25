# Crie uma função exibir_perfil() que receba o nome, a idade e o tipo de conta de um utilizador. 
# O tipo de conta deve ter "Gratuito" como valor padrão. 
# Teste a função com e sem informar o tipo de conta.

# Utilizador: Ana Silva | Idade: 28 | Plano: Gratuito
# Utilizador: João Santos | Idade: 35 | Plano: Premium

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

def exibir_perfil(plano="Gratuito"):
    print(f"\nUtilizador: {nome} | Idade: {idade} | Plano: {plano}")

exibir_perfil()
exibir_perfil("Premium")