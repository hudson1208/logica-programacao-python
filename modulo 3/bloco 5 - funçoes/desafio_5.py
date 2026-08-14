# ### Desafio 05 — Sistema modularizado de estoque

# Desenvolva um sistema de gerenciamento de estoque utilizando uma lista de dicionários para armazenar os produtos.

# Organize o sistema em funções responsáveis por:

# - exibir o menu;
# - cadastrar produtos;
# - listar produtos;
# - pesquisar produtos;
# - atualizar o estoque;
# - remover produtos.

# Cada produto deverá possuir, no mínimo, nome, preço e quantidade em estoque.

# O programa deverá utilizar um menu para controlar as operações e permanecer em execução até que o usuário escolha encerrar.

# As funções devem receber os dados necessários por parâmetros e retornar resultados quando apropriado, evitando responsabilidades excessivas em uma única função.

def exibir_menu() -> None:
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Pesquisar produto")
    print("4 - Atualizar estoque")
    print("5 - Remover produto")
    print("0 - Encerrar")


def cadastrar_produto(nome: str, preco: float, quantidade: int) -> dict:
    produto: dict = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    return produto


def listar_produtos(produtos: list[dict]) -> None:
    if len(produtos) == 0:
        print("\nNenhum produto cadastrado.")
        return

    print("\n===== PRODUTOS CADASTRADOS =====")

    for produto in produtos:
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade em estoque: {produto['quantidade']}")
        print("-" * 30)


def pesquisar_produto(produtos: list[dict], nome_pesquisado: str) -> dict | None:
    for produto in produtos:
        if produto["nome"].lower() == nome_pesquisado.lower():
            return produto

    return None


def atualizar_estoque(
    produtos: list[dict],
    nome_produto: str,
    nova_quantidade: int
) -> bool:
    produto: dict | None = pesquisar_produto(produtos, nome_produto)

    if produto is not None:
        produto["quantidade"] = nova_quantidade
        return True

    return False


def remover_produto(produtos: list[dict], nome_produto: str) -> bool:
    produto: dict | None = pesquisar_produto(produtos, nome_produto)

    if produto is not None:
        produtos.remove(produto)
        return True

    return False


produtos: list[dict] = []

while True:
    exibir_menu()

    opcao: str = input("Escolha uma opção: ")

    if opcao == "1":
        nome: str = input("Digite o nome do produto: ")
        preco: float = float(input("Digite o preço do produto: "))
        quantidade: int = int(input("Digite a quantidade em estoque: "))

        produto: dict = cadastrar_produto(nome, preco, quantidade)
        produtos.append(produto)

        print("\nProduto cadastrado com sucesso!")

    elif opcao == "2":
        listar_produtos(produtos)

    elif opcao == "3":
        nome_busca: str = input("Digite o nome do produto que deseja pesquisar: ")

        produto_encontrado: dict | None = pesquisar_produto(produtos, nome_busca)

        if produto_encontrado is not None:
            print("\nProduto encontrado:")
            print(f"Nome: {produto_encontrado['nome']}")
            print(f"Preço: R$ {produto_encontrado['preco']:.2f}")
            print(f"Quantidade em estoque: {produto_encontrado['quantidade']}")
        else:
            print("\nProduto não encontrado.")

    elif opcao == "4":
        nome_busca: str = input("Digite o nome do produto que deseja atualizar: ")

        produto_encontrado: dict | None = pesquisar_produto(produtos, nome_busca)

        if produto_encontrado is not None:
            nova_quantidade: int = int(input("Digite a nova quantidade em estoque: "))

            atualizado: bool = atualizar_estoque(
                produtos,
                nome_busca,
                nova_quantidade
            )

            if atualizado:
                print("\nEstoque atualizado com sucesso!")
        else:
            print("\nProduto não encontrado.")

    elif opcao == "5":
        nome_busca: str = input("Digite o nome do produto que deseja remover: ")

        produto_encontrado: dict | None = pesquisar_produto(produtos, nome_busca)

        if produto_encontrado is not None:
            confirmacao: str = input(
                f"Tem certeza que deseja remover {produto_encontrado['nome']}? (s/n): "
            ).lower()

            if confirmacao == "s":
                removido: bool = remover_produto(produtos, nome_busca)

                if removido:
                    print("\nProduto removido com sucesso!")
            else:
                print("\nRemoção cancelada.")
        else:
            print("\nProduto não encontrado.")

    elif opcao == "0":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida. Tente novamente.")