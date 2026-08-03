# ### Atividade 11 — Estatísticas da turma

# Solicite quatro notas, armazenando-as em uma lista. Ao final, apresente:

# - todas as notas;
# - maior nota;
# - menor nota;
# - média da turma.

# Utilize as funções nativas da linguagem sempre que possível.

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

print("\nNotas da turma:", notas)
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
print("Média da turma:", sum(notas) / len(notas))