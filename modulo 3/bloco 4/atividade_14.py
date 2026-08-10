# ### Atividade 14 — Lista de produtos

# Cadastre cinco produtos utilizando uma lista de dicionários. Para cada produto, solicite
# ao usuário o nome, a categoria, o preço e a quantidade em estoque. Ao final, percorra a 
# lista e apresente todos os produtos cadastrados.

produtos = []

for i in range(5):
    print(f"\nCadastro do {i + 1}º produto")

    nome = input("Nome: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))
    estoque = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)

print("\n PRODUTOS CADASTRADOS")

for produto in produtos:
    print(f"\nNome: {produto['nome']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Estoque: {produto['estoque']} unidades")