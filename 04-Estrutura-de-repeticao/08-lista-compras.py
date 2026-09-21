compras = []

produto = input("Digite um produto (ou 'fim' para terminar): ")

while produto != "fim":
    compras.append(produto)

    produto = input("Digite outro produto (ou 'fim' para terminar): ")

print("\nLista de compras:\n")

for produtos in compras:
    print(f"- {produtos}")