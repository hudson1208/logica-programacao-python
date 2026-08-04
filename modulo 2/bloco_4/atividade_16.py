# ### Atividade 16 — Diário de Classe

# Cadastre o nome de cinco alunos e a média final de cada um.

# Após o cadastro, apresente um relatório contendo:

# - nome;
# - média;
# - situação (Aprovado, Recuperação ou Reprovado).

# Ao final, informe:

# - quantidade de aprovados;
# - quantidade de alunos em recuperação;
# - quantidade de reprovados.

nomes = []
medias = []

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    media = float(input("Digite a média final: "))

    nomes.append(nome)
    medias.append(media)

print("\n=== RELATÓRIO FINAL ===")

for i in range(5):
    if medias[i] >= 7:
        situacao = "Aprovado"
        aprovados += 1
    elif medias[i] >= 5:
        situacao = "Recuperação"
        recuperacao += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    print(f"Nome: {nomes[i]}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")
    print("-" * 20)

print("\n=== RESUMO ===")
print(f"Quantidade de aprovados: {aprovados}")
print(f"Quantidade em recuperação: {recuperacao}")
print(f"Quantidade de reprovados: {reprovados}")