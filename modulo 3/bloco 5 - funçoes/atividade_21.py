### Atividade 21 — Cadastro de produto

# Solicite ao usuário o nome, o preço e a quantidade em estoque de
# um produto. Crie uma função que receba esses dados como parâmetros
# e retorne um dicionário representando o produto. Ao final, apresente
# o cadastro criado.

def cadastrar_produto(nome: str, preco: float, quantidade: int) -> dict:
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    return produto


nome_produto: str = input("Digite o nome do produto: ")
preco_produto: float = float(input("Digite o preço do produto: "))
quantidade_produto: int = int(input("Digite a quantidade em estoque: "))

produto_cadastrado: dict = cadastrar_produto(
    nome_produto,
    preco_produto,
    quantidade_produto
)

print("\nProduto cadastrado:")
print(f"Nome: {produto_cadastrado['nome']}")
print(f"Preço: R$ {produto_cadastrado['preco']:.2f}")
print(f"Quantidade em estoque: {produto_cadastrado['quantidade']}")