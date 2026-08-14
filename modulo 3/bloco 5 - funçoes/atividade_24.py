### Atividade 24 — Análise de notas

# Solicite ao usuário cinco notas e armazene-as em uma lista. Crie uma função
# que receba essa lista e retorne a maior nota, a menor nota e a média.
# Utilize desempacotamento para receber e apresentar os resultados.

def analisar_notas(notas: list[float]) -> tuple[float, float, float]:
    maior_nota: float = max(notas)
    menor_nota: float = min(notas)
    media: float = sum(notas) / len(notas)

    return maior_nota, menor_nota, media


notas: list[float] = []

for i in range(5):
    nota: float = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)


maior, menor, media = analisar_notas(notas)

print("\nAnálise das notas:")
print(f"Notas informadas: {notas}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média: {media:.2f}")