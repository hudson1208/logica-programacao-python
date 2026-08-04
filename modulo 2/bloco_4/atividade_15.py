# <!-- ### Atividade 15 — Controle de Estoque

# Cadastre cinco produtos e suas respectivas quantidades em estoque.

# Ao final, apresente uma mensagem informando quais produtos possuem quantidade igual ou inferior a cinco unidades. -->

produtos = []
quantidades = []

for i in range(5):
    produto = input(f"Digite o nome do {i + 1}º produto: ")
    quantidade = int(input(f"Digite a quantidade em estoque de {produto}: "))

    produtos.append(produto)
    quantidades.append(quantidade)

print("\nProdutos com quantidade igual ou inferior a 5 unidades:")

encontrou = False

for i in range(5):
    if quantidades[i] <= 5:
        print(f"{produtos[i]} - {quantidades[i]} unidades")
        encontrou = True

if not encontrou:
    print("Nenhum produto possui quantidade igual ou inferior a 5 unidades.")







    