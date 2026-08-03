# ### Atividade 13 — Controle de produtos

# Crie um menu com as opções:

# ```
# 1 - Adicionar produto
# 2 - Remover produto
# 3 - Listar produtos
# 4 - Encerrar
# ```

# Os produtos deverão ser armazenados em uma lista durante a execução do programa.

# Utilize estruturas de repetição e `match-case ` para controlar o menu.

produtos = []

while True:
    print("\n=== CONTROLE DE PRODUTOS ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Encerrar")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            produto = input("Digite o nome do produto: ")
            produtos.append(produto)
            print("Produto adicionado com sucesso!")

        case "2":
            produto = input("Digite o nome do produto a remover: ")
            if produto in produtos:
                produtos.remove(produto)
                print("Produto removido com sucesso!")
            else:
                print("Produto não encontrado!")

        case "3":
            if produtos:
                print("\nLista de produtos:")
                for i, produto in enumerate(produtos, start=1):
                    print(f"{i}. {produto}")
            else:
                print("Nenhum produto cadastrado.")

        case "4":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida! Tente novamente.")









            