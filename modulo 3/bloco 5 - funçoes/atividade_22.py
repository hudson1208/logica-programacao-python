### Atividade 22 — Busca de produto

# Cadastre produtos utilizando uma lista de dicionários. Crie uma função que receba
# a lista de produtos e o nome que será pesquisado. A função deverá retornar o
# dicionário correspondente quando o produto for encontrado ou `None` quando não existir.

def buscar_produto(produtos: list[dict], nome_pesquisado: str) -> dict | None:
    for produto in produtos:
        if produto["nome"].lower() == nome_pesquisado.lower():
            return produto

    return None


produtos: list[dict] = [
    {"nome": "Mouse", "preco": 59.90, "quantidade": 15},
    {"nome": "Teclado", "preco": 120.00, "quantidade": 8},
    {"nome": "Monitor", "preco": 899.90, "quantidade": 5}
]

nome_busca: str = input("Digite o nome do produto que deseja buscar: ")

produto_encontrado: dict | None = buscar_produto(produtos, nome_busca)

if produto_encontrado is not None:
    print("\nProduto encontrado:")
    print(f"Nome: {produto_encontrado['nome']}")
    print(f"Preço: R$ {produto_encontrado['preco']:.2f}")
    print(f"Quantidade em estoque: {produto_encontrado['quantidade']}")
else:
    print("\nProduto não encontrado.")