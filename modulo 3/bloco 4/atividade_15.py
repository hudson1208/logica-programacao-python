# ### Atividade 15 — Pesquisa de contatos

# Cadastre contatos em uma lista de dicionários, armazenando nome, telefone e e-mail.
# Em seguida, solicite ao usuário o nome de um contato, pesquise-o na lista e apresente
# seus dados. Caso o contato não seja encontrado, informe ao usuário.

contatos = []

# Cadastro de cinco contatos
for i in range(5):
    print(f"\nCadastro do {i + 1}º contato")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)

nome_pesquisado = input("\nDigite o nome do contato que deseja pesquisar: ")

contato_encontrado = False

for contato in contatos:
    if contato["nome"].lower() == nome_pesquisado.lower():
        print("\nContato encontrado!")
        print("Nome:", contato["nome"])
        print("Telefone:", contato["telefone"])
        print("E-mail:", contato["email"])

        contato_encontrado = True
        break

if contato_encontrado == False:
    print("\nContato não encontrado.")
