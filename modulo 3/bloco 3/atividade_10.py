# ### Atividade 10 — Atualização de produto

# Solicite ao usuário o nome, o preço e a quantidade em estoque 
# de um produto e armazene essas informações em um dicionário. 
# Em seguida, adicione a categoria, atualize o preço, aumente a
# quantidade em estoque e, ao final, apresente todos os dados atualizados.

produto = {}

produto["nome"] = input("Digite o nome do produto: ")
produto["preco"] = float(input("Digite o preço do produto: R$ "))
produto["quantidade"] = int(input("Digite a quantidade em estoque: "))

produto["categoria"] = input("Digite a categoria do produto: ")

produto["preco"] = float(input("Digite o novo preço do produto: R$ "))

aumento = int(input("Digite a quantidade que será adicionada ao estoque: "))
produto["quantidade"] += aumento

print("\n--- Dados atualizados do produto ---")
print("Nome:", produto["nome"])
print(f'Preço: R$ {produto["preco"]:.2f}')
print("Quantidade em estoque:", produto["quantidade"])
print("Categoria:", produto["categoria"])