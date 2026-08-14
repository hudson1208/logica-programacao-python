### Atividade 25 — Agenda de contatos

# Desenvolva uma agenda utilizando uma lista de dicionários, em que cada contato
# armazene nome, telefone e e-mail. Organize o programa em funções que permitam
# cadastrar novos contatos, listar os registros existentes, realizar pesquisas,
# atualizar informações e remover um contato.

def exibir_menu() -> None:
    print("\n===== AGENDA DE CONTATOS =====")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Pesquisar contato")
    print("4 - Atualizar contato")
    print("5 - Remover contato")
    print("0 - Encerrar")


def cadastrar_contato(nome: str, telefone: str, email: str) -> dict:
    contato: dict = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    return contato


def listar_contatos(contatos: list[dict]) -> None:
    if len(contatos) == 0:
        print("\nNenhum contato cadastrado.")
        return

    print("\n===== CONTATOS CADASTRADOS =====")

    for contato in contatos:
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")
        print("-" * 30)


def pesquisar_contato(contatos: list[dict], nome_pesquisado: str) -> dict | None:
    for contato in contatos:
        if contato["nome"].lower() == nome_pesquisado.lower():
            return contato

    return None


def atualizar_contato(
    contatos: list[dict],
    nome_pesquisado: str,
    novo_telefone: str,
    novo_email: str
) -> bool:
    contato: dict | None = pesquisar_contato(contatos, nome_pesquisado)

    if contato is not None:
        contato["telefone"] = novo_telefone
        contato["email"] = novo_email
        return True

    return False


def remover_contato(contatos: list[dict], nome_pesquisado: str) -> bool:
    contato: dict | None = pesquisar_contato(contatos, nome_pesquisado)

    if contato is not None:
        contatos.remove(contato)
        return True

    return False


contatos: list[dict] = []

while True:
    exibir_menu()

    opcao: str = input("Escolha uma opção: ")

    if opcao == "1":
        nome: str = input("Digite o nome do contato: ")
        telefone: str = input("Digite o telefone do contato: ")
        email: str = input("Digite o e-mail do contato: ")

        contato: dict = cadastrar_contato(nome, telefone, email)
        contatos.append(contato)

        print("\nContato cadastrado com sucesso!")

    elif opcao == "2":
        listar_contatos(contatos)

    elif opcao == "3":
        nome_busca: str = input("Digite o nome do contato que deseja pesquisar: ")

        contato_encontrado: dict | None = pesquisar_contato(contatos, nome_busca)

        if contato_encontrado is not None:
            print("\nContato encontrado:")
            print(f"Nome: {contato_encontrado['nome']}")
            print(f"Telefone: {contato_encontrado['telefone']}")
            print(f"E-mail: {contato_encontrado['email']}")
        else:
            print("\nContato não encontrado.")

    elif opcao == "4":
        nome_busca: str = input("Digite o nome do contato que deseja atualizar: ")

        contato_encontrado: dict | None = pesquisar_contato(contatos, nome_busca)

        if contato_encontrado is not None:
            novo_telefone: str = input("Digite o novo telefone: ")
            novo_email: str = input("Digite o novo e-mail: ")

            atualizado: bool = atualizar_contato(
                contatos,
                nome_busca,
                novo_telefone,
                novo_email
            )

            if atualizado:
                print("\nContato atualizado com sucesso!")
        else:
            print("\nContato não encontrado.")

    elif opcao == "5":
        nome_busca: str = input("Digite o nome do contato que deseja remover: ")

        contato_encontrado: dict | None = pesquisar_contato(contatos, nome_busca)

        if contato_encontrado is not None:
            confirmacao: str = input(
                f"Tem certeza que deseja remover {contato_encontrado['nome']}? (s/n): "
            ).lower()


