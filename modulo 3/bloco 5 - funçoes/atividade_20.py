### Atividade 20 — Classificação de aluno

# Solicite ao usuário as notas de um aluno e desenvolva funções separadas para calcular a média, classificar
# o resultado e apresentar as informações. Considere: média maior ou igual a `7` → Aprovado; média maior ou
# igual a `5` e menor que `7` → Recuperação; média menor que `5` → Reprovado. Organize o programa de forma
# que cada função possua uma responsabilidade específica.

def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)


def classificar_aluno(media: float) -> str:
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def apresentar_resultado(notas: list[float], media: float, classificacao: str) -> None:
    print("\nResultado do aluno")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Classificação: {classificacao}")


nota1: float = float(input("Digite a primeira nota: "))
nota2: float = float(input("Digite a segunda nota: "))
nota3: float = float(input("Digite a terceira nota: "))

notas_aluno: list[float] = [nota1, nota2, nota3]

media_aluno: float = calcular_media(notas_aluno)
classificacao_aluno: str = classificar_aluno(media_aluno)

apresentar_resultado(
    notas_aluno,
    media_aluno,
    classificacao_aluno
)