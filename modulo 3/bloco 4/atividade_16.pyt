### Atividade 16 — Atualização de estoque

# Cadastre três produtos em uma lista de dicionários, armazenando nome,
# preço e quantidade em estoque. Em seguida, solicite ao usuário o nome
# de um produto, localize o registro correspondente e permita atualizar
# sua quantidade em estoque. Caso o produto não seja encontrado, informe
# ao usuário. Ao final, apresente os dados atualizados.

produtos = [
    {"nome": "Arroz", "preco": 25.50, "quantidade": 10},
    {"nome": "Feijao", "preco": 8.90, "quantidade": 15},
    {"nome": "Macarrao", "preco": 4.50, "quantidade": 20}
]

nome_produto = input("Digite o nome do produto: ")

encontrado = False

for produto in produtos:
    if produto["nome"].lower() == nome_produto.lower():
        nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
        produto["quantidade"] = nova_quantidade
        encontrado = True
        print("Estoque atualizado com sucesso!")
        break

if not encontrado:
    print("Produto não encontrado.")

print("\nProdutos cadastrados:")
for produto in produtos:
    print(produto)