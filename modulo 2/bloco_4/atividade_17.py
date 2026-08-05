# ### Atividade 17 — Pesquisa de Produtos

# Cadastre diversos produtos.

# O cadastro deverá continuar até que o usuário digite **fim**.

# Depois, solicite o nome de um produto e informe se ele está cadastrado.

# Caso exista, informe sua posição na lista.

produtos = []

while True:
    produto = input("Digite o nome do produto ou 'fim' para encerrar: ")

    if produto.lower() == "fim":
        break

    produtos.append(produto)

pesquisa = input("Digite o nome do produto que deseja pesquisar: ")

if pesquisa in produtos:
    posicao = produtos.index(pesquisa)
    print(f"O produto '{pesquisa}' está cadastrado.")
    print(f"Ele está na posição {posicao} da lista.")
else:
    print(f"O produto '{pesquisa}' não está cadastrado.")