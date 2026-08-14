### Atividade 23 — Atualização de estoque

# Cadastre produtos em uma lista de dicionários. Crie uma função que receba
# a lista, o nome do produto e a nova quantidade em estoque. Caso o produto
# seja encontrado, atualize sua quantidade e retorne `True`. Caso contrário,
# retorne `False`.

def atualizar_estoque(
    produtos: list[dict],
    nome_produto: str,
    nova_quantidade: int
) -> bool:
    for produto in produtos:
        if produto["nome"].lower() == nome_produto.lower():
            produto["quantidade"] = nova_quantidade
            return True

    return False


produtos: list[dict] = [
    {"nome": "Mouse", "preco": 59.90, "quantidade": 15},
    {"nome": "Teclado", "preco": 120.00, "quantidade": 8},
    {"nome": "Monitor", "preco": 899.90, "quantidade": 5}
]

nome_busca: str = input("Digite o nome do produto: ")
quantidade_atualizada: int = int(input("Digite a nova quantidade em estoque: "))

foi_atualizado: bool = atualizar_estoque(
    produtos,
    nome_busca,
    quantidade_atualizada
)

if foi_atualizado:
    print("\nEstoque atualizado com sucesso!")
else:
    print("\nProduto não encontrado.")

print("\nLista de produtos:")
for produto in produtos:
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print("-" * 30)
