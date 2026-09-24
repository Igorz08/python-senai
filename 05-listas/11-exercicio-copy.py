# Crie uma lista com algumas linguagens de programação.

# Crie uma cópia dessa lista usando copy().

# Use um for para mostrar as linguagens da lista copiada.

# Lista de linguagens
linguagens = ["Python", "JavaScript", "Java", "PHP"]

copia = linguagens.copy()

print("\nLista copiada:\n")

for lista in copia:
    print(f"- {lista}")