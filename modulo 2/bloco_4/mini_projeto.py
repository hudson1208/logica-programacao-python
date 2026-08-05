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

livros = []

while True:
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Remover livro")
    print("5 - Encerrar")

    opcao = input("Escolha uma opção: ")


