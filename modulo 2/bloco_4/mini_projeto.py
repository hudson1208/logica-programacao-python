"""
# ### Mini Projeto — Sistema de Biblioteca

# Desenvolva um programa que simule o cadastro simplificado de livros de uma biblioteca.

# O sistema deverá apresentar um menu com as seguintes opções:

# ```
# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Pesquisar livro
# 4 - Remover livro
# 5 - Encerrar
# ```

# Os livros deverão ser armazenados em uma lista durante toda a execução do programa.

# Ao pesquisar ou remover um livro inexistente, o sistema deverá informar o usuário.
"""

livros = []


def cadastrar_livro():
    titulo = input("\nDigite o título do livro: ").strip()

    if titulo == "":
        print("O título do livro não pode ficar vazio.")
        return

    livros.append(titulo)
    print(f'Livro "{titulo}" cadastrado com sucesso!')


def listar_livros():
    print("\n--- LIVROS CADASTRADOS ---")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for numero, livro in enumerate(livros, start=1):
        print(f"{numero} - {livro}")


def pesquisar_livro():
    titulo_pesquisado = input(
        "\nDigite o título do livro que deseja pesquisar: "
    ).strip()

    for livro in livros:
        if livro.lower() == titulo_pesquisado.lower():
            print(f'Livro encontrado: "{livro:}"')
            return

    print(f'O livro "{titulo_pesquisado}" não foi encontrado.')


def remover_livro():
    titulo_pesquisado = input(
        "\nDigite o título do livro que deseja remover: "
    ).strip()

    for livro in livros:
        if livro.lower() == titulo_pesquisado.lower():
            livros.remove(livro)
            print(f'Livro "{livro}" removido com sucesso!')
            return

    print(f'O livro "{titulo_pesquisado}" não foi encontrado.')


while True:
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Remover livro")
    print("5 - Encerrar")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        pesquisar_livro()

    elif opcao == "4":
        remover_livro()

    elif opcao == "5":
        print("\nXii fechou o sistema, que pena. Xaaau!")
        break

    else:
        print("\nOpção inválida. Digite um número de 1 a 5.")


