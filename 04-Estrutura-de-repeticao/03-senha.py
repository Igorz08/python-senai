# Define a senha correta
senha_correta = "1234"

# Solicita a senha ao usuario
senha = input("Digite a senha: ")

# Enquanto a senha estiver errada
while senha != senha_correta:

    # Informa que a senha está erradA
    print("Senha incorreta.")

    # Solicita a senha novamente
    senha = input("Digite a senha novamente: ")

# Quando a condição ficar falsa, a está correta
print("Senha correta, acesso permitido")