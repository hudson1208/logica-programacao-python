# ### Atividade 18 — Ranking de Notas

# Cadastre as notas de dez estudantes.

# Ao final:

# - apresente todas as notas em ordem crescente;
# - apresente todas as notas em ordem decrescente;
# - informe a maior nota;
# - informe a menor nota;
# - informe a média da turma.

notas = []

for i in range(10):
    nota = float(input(f"Digite a nota do {i + 1}º estudante: "))
    notas.append(nota)

crescente = sorted(notas)

decrescente = sorted(notas, reverse=False)

maior_nota = max(notas)
menor_nota = min(notas)

media = sum(notas) / len(notas)

print("\nNotas em ordem crescente:")
print(crescente)

print("\nNotas em ordem decrescente:")
print(decrescente)

print(f"\nMaior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Média da turma: {media:.2f}")