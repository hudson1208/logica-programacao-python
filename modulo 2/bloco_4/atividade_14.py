# ### Atividade 14 — Cadastro de Produtos

# Desenvolva um programa que permita cadastrar dez produtos. Ao final, apresente todos os produtos cadastrados em ordem alfabética.

produtos = []

for i in range(10):
    produto = input(f"Digite o nome do {i + 1}º produto: ")
    produtos.append(produto)

produtos.sort()

print("\nProdutos cadastrados em ordem alfabética:")

for produto in produtos:
    print(produto)