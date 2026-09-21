# Cria um programa que permita ao utilizador fazer vários pedidos numa lanchonete.

# O programa deve pedir ao utilizador o nome de um produto.

# Enquanto o utilizador não escrever sair, o programa deve continuar a pedir novos produtos.

# Quando o utilizador escrever sair, o programa deve mostrar:

#   .Quantos produtos foram pedidos;
#   .Uma mensagem a indicar que o pedido foi finalizado.

# Digite o produto que deseja pedir: hambúrguer
# Digite o produto que deseja pedir: batata
# Digite o produto que deseja pedir: refrigerante
# Digite o produto que deseja pedir: sair

# Pedido finalizado!
# Você pediu 3 produtos.

compras = []
quantPedidos = 0

produto = input("Digite um produto (ou 'sair' para finalizar pedido): ")

while produto != "sair":
    compras.append(produto)

    quantPedidos = quantPedidos + 1

    produto = input("Digite outro produto (ou 'sair' para finalizar pedido): ")

print("\nPedido finalizado!")
print("Lista de produtos:\n")

for ListaProdutos in compras:
    print(f"- {ListaProdutos}")

print(f"\nVocê pediu {quantPedidos} produtos.")