# ### Desafio 03 — Cadastro de livro

# Desenvolva um programa para gerenciar o cadastro de um livro. Solicite ao usuário o título, o 
# autor, o ano, a quantidade de páginas e a disponibilidade e armazene essas informações em um dicionário.
# O programa deverá apresentar um menu que permita consultar uma informação, alterar um valor, adicionar
# uma nova informação, remover uma informação, visualizar todo o cadastro e encerrar o programa.
# Durante as operações, verifique a existência das chaves quando necessário e utilize os recursos estudados,
# como `get()`, `in`, `not in`, `items()`, `update()` e `pop()`, juntamente com estruturas condicionais e de repetição.
# O programa deverá permanecer em execução até que o usuário escolha a opção de sair.

# Desafio 03 — Cadastro de livro

livro = {}

# Cadastro inicial do livro
livro["titulo"] = input("Digite o título do livro: ")
livro["autor"] = input("Digite o autor do livro: ")
livro["ano"] = int(input("Digite o ano de publicação: "))
livro["paginas"] = int(input("Digite a quantidade de páginas: "))
livro["disponibilidade"] = input("O livro está disponível? Sim/Não: ")

while True:
    print("\n===== MENU DO CADASTRO DE LIVRO =====")
    print("1 - Consultar uma informação")
    print("2 - Alterar um valor")
    print("3 - Adicionar uma nova informação")
    print("4 - Remover uma informação")
    print("5 - Visualizar todo o cadastro")
    print("6 - Encerrar o programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        chave = input("Digite a chave que deseja consultar: ")

        # Usando get()
        valor = livro.get(chave)

        if valor is not None:
            print(f"{chave}: {valor}")
        else:
            print("Essa informação não existe no cadastro.")

    elif opcao == "2":
        chave = input("Digite a chave que deseja alterar: ")

        # Usando in
        if chave in livro:
            novo_valor = input("Digite o novo valor: ")

            # Usando update()
            livro.update({chave: novo_valor})

            print("Informação alterada com sucesso.")
        else:
            print("Essa chave não existe no cadastro.")

    elif opcao == "3":
        chave = input("Digite o nome da nova informação: ")

        # Usando not in
        if chave not in livro:
            valor = input("Digite o valor dessa informação: ")

            # Usando update()
            livro.update({chave: valor})

            print("Nova informação adicionada com sucesso.")
        else:
            print("Essa informação já existe no cadastro.")

    elif opcao == "4":
        chave = input("Digite a chave que deseja remover: ")

        # Verificando se a chave existe
        if chave in livro:
            livro.pop(chave)
            print("Informação removida com sucesso.")
        else:
            print("Essa chave não existe no cadastro.")

    elif opcao == "5":
        print("\n===== CADASTRO ATUALIZADO DO LIVRO =====")

        # Usando items()
        for chave, valor in livro.items():
            print(f"{chave}: {valor}")

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Escolha uma opção de 1 a 6.")