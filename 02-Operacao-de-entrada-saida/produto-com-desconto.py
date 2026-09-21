# Entrada de dados basicos
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto (%): "))

# Processamento computacional
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

# Saída de informação
print(f"\nPreço digitado: R${preco:.2f}")
print(f"Desconto digitado: {desconto:.1f}%")
print(f"Valor de desconto: R${valor_desconto:.2f}")
print(f"Valor final: R${preco_final:.2f}")