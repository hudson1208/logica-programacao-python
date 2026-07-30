# ## Atividade 04 — Menu do sistema

# Crie um menu com as opções:

# ```
# 1 - Novo cadastro
# 2 - Consultar cadastro
# 3 - Atualizar cadastro
# 4 - Remover cadastro
# ```

# Utilize `match-case` para apresentar uma mensagem correspondente à opção escolhida e trate entradas inválidas.

print("=== MENU ===")
print("1 - Novo cadastro")
print("2 - Consultar cadastro")
print("3 - Atualizar cadastro")
print("4 - Remover cadastro")

opcao = input("Escolha uma opção: ")

match opcao:
    case "1":
        print("Novo cadastro selecionado.")
    case "2":
        print("Consultar cadastro selecionado.")
    case "3":
        print("Atualizar cadastro selecionado.")
    case "4":
        print("Remover cadastro selecionado.")
    case _:
        print("Opção inválida! Escolha uma opção de 1 a 4.")