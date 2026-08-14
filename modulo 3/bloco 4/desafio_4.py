### Desafio 04 — Sistema de biblioteca

# Desenvolva um sistema de gerenciamento de livros utilizando uma lista de dicionários. Cada livro deverá possuir título, autor, ano e disponibilidade.
# O sistema deverá apresentar um menu que permita cadastrar livros, listar todos os registros, pesquisar um livro, atualizar sua disponibilidade, remover
# um livro e encerrar o programa.Cada livro deverá ser representado por um dicionário e armazenado na lista principal. Durante as operações, o programa
# deverá informar quando um livro não for encontrado e permanecer em execução até que o usuário escolha a opção de encerrar.O desafio deverá integrar os
#  conceitos estudados de listas, dicionários, estruturas compostas, condicionais e estruturas de repetição.

def exibir_menu() -> None:
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Atualizar disponibilidade")
    print("5 - Remover livro")
    print("0 - Encerrar")


def cadastrar_livro(
    titulo: str,
    autor: str,
    ano: int,
    disponibilidade: bool
) -> dict:
    livro: dict = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponibilidade": disponibilidade
    }

    return livro


def listar_livros(livros: list[dict]) -> None:
    if len(livros) == 0:
        print("\nNenhum livro cadastrado.")
        return

    print("\n===== LISTA DE LIVROS =====")

    for livro in livros:
        disponibilidade: str = "Disponível" if livro["disponibilidade"] else "Indisponível"

        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"Disponibilidade: {disponibilidade}")
        print("-" * 30)


def pesquisar_livro(livros: list[dict], titulo_pesquisado: str) -> dict | None:
    for livro in livros:
        if livro["titulo"].lower() == titulo_pesquisado.lower():
            return livro

    return None


def atualizar_disponibilidade(
    livros: list[dict],
    titulo_livro: str,
    nova_disponibilidade: bool
) -> bool:
    livro: dict | None = pesquisar_livro(livros, titulo_livro)

    if livro is not None:
        livro["disponibilidade"] = nova_disponibilidade
        return True

    return False


def remover_livro(livros: list[dict], titulo_livro: str) -> bool:
    livro: dict | None = pesquisar_livro(livros, titulo_livro)

    if livro is not None:
        livros.remove(livro)
        return True

    return False


livros: list[dict] = []

while True:
    exibir_menu()

    opcao: str = input("Escolha uma opção: ")

    if opcao == "1":
        titulo: str = input("Digite o título do livro: ")
        autor: str = input("Digite o autor do livro: ")
        ano: int = int(input("Digite o ano do livro: "))

        resposta: str = input("O livro está disponível? (s/n): ").lower()

        if resposta == "s":
            disponibilidade: bool = True
        else:
            disponibilidade: bool = False

        livro: dict = cadastrar_livro(
            titulo,
            autor,
            ano,
            disponibilidade
        )

        livros.append(livro)

        print("\nLivro cadastrado com sucesso!")

    elif opcao == "2":
        listar_livros(livros)

    elif opcao == "3":
        titulo_busca: str = input("Digite o título do livro que deseja pesquisar: ")

        livro_encontrado: dict | None = pesquisar_livro(livros, titulo_busca)

        if livro_encontrado is not None:
            disponibilidade: str = (
                "Disponível"
                if livro_encontrado["disponibilidade"]
                else "Indisponível"
            )

            print("\nLivro encontrado:")
            print(f"Título: {livro_encontrado['titulo']}")
            print(f"Autor: {livro_encontrado['autor']}")
            print(f"Ano: {livro_encontrado['ano']}")
            print(f"Disponibilidade: {disponibilidade}")
        else:
            print("\nLivro não encontrado.")

    elif opcao == "4":
        titulo_busca: str = input("Digite o título do livro que deseja atualizar: ")

        livro_encontrado: dict | None = pesquisar_livro(livros, titulo_busca)

        if livro_encontrado is not None:
            resposta: str = input("O livro está disponível agora? (s/n): ").lower()

            if resposta == "s":
                nova_disponibilidade: bool = True
            else:
                nova_disponibilidade: bool = False

            atualizado: bool = atualizar_disponibilidade(
                livros,
                titulo_busca,
                nova_disponibilidade
            )

            if atualizado:
                print("\nDisponibilidade atualizada com sucesso!")
        else:
            print("\nLivro não encontrado.")

    elif opcao == "5":
        titulo_busca: str = input("Digite o título do livro que deseja remover: ")

        livro_encontrado: dict | None = pesquisar_livro(livros, titulo_busca)

        if livro_encontrado is not None:
            confirmacao: str = input(
                f"Tem certeza que deseja remover '{livro_encontrado['titulo']}'? (s/n): "
            ).lower()

            if confirmacao == "s":
                removido: bool = remover_livro(livros, titulo_busca)

                if removido:
                    print("\nLivro removido com sucesso!")
            else:
                print("\nRemoção cancelada.")
        else:
            print("\nLivro não encontrado.")

    elif opcao == "0":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida. Tente novamente.")