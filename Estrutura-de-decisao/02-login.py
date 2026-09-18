# Solicita o login do usuário
login = input("Digite seu login: ")

# Solicita a senha do usuário
senha = input("Digite seu senha: ")

# Verifica se o login e a senha estão corretos
if login == "admin" and senha == "1234":
    print("\nSeja bem-vindo, administrador!")
else:
    print("\nLogin ou senha incorretos")