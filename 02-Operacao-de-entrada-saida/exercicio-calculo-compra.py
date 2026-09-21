# Crie um programa que solicite o nome de um produto, 
# seu preço e a quantidade comprada. Depois, calcule o valor total da compra
# e exiba o nome do produto e o valor total.

# Entrada de dados
prod = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$"))
quant = int(input("Digite a quantidade dos produtos comprados: "))

# Processamento computacional
preco_total = preco * quant

# Saída de informação
print(f"\nProduto: {prod}\nValor total: R${preco_total:.2f}")