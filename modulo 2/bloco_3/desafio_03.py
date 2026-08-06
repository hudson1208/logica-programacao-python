"""# ### Desafio 03 — Boletim da Turma

# Desenvolva um programa que permita cadastrar vários alunos. Para cada estudante, informe seu nome e quatro notas. Ao final do cadastro, apresente um relatório contendo:

# - nome de cada aluno;
# - média final;
# - situação (Aprovado, Recuperação ou Reprovado);
# - maior média da turma;
# - menor média da turma;
# - média geral da turma.

# Utilize listas, estruturas condicionais e laços de repetição para organizar a solução.
"""

alunos = []

while True:
    nome = input("Digite o nome do aluno: ")

    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i + 1}ª nota de {nome}: "))
        notas.append(nota)

    media = sum(notas) / 4

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (S/N): ").upper()

    if continuar != "S":
        break


print("\n===== RELATÓRIO DA TURMA =====")

soma_medias = 0
maior_media = alunos[0]["media"]
menor_media = alunos[0]["media"]

for aluno in alunos:
    print(f"\nAluno: {aluno['nome']}")
    print(f"Média final: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")

    soma_medias += aluno["media"]

    if aluno["media"] > maior_media:
        maior_media = aluno["media"]

    if aluno["media"] < menor_media:
        menor_media = aluno["media"]

media_geral = soma_medias / len(alunos)

print("\n===== RESUMO DA TURMA =====")
print(f"Maior média da turma: {maior_media:.2f}")
print(f"Menor média da turma: {menor_media:.2f}")
print(f"Média geral da turma: {media_geral:.2f}")