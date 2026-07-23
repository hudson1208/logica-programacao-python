# Entrada de dados
nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário: R$ "))
quantidade = int(input("Digite a quantidade: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Cálculos    
subtotal = preco_unitario * quantidade
valor_desconto = subtotal * percentual_desconto / 100
total = subtotal - valor_desconto

# Verificações  
quantidade_maior_zero = quantidade > 0 # Comparação
total_maior_100 = total > 100 # Comparação
contem_letra_a = "a" in nome_produto.lower() # Associação
desconto_valido = percentual_desconto is not None # Identidade

print("\n===== RESUMO DA COMPRA =====")
print(f"Produto: {nome_produto}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Total da compra: R$ {total:.2f}")
print("\n===== VERIFICAÇÕES =====")
print(f"Quantidade maior que zero? {quantidade_maior_zero}")
print(f"Total maior que R$ 100,00? {total_maior_100}")
print(f"Nome contém a letra 'a'? {contem_letra_a}")
print(f"Desconto é diferente de None? {desconto_valido}")
print(f"Compra válida? {quantidade_maior_zero and total > 0}")