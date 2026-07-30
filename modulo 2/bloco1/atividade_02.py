# ## Atividade 02 — Classificação de notas

# Solicite a nota final de um estudante e informe sua situação conforme os critérios abaixo:

# - nota maior ou igual a 7: aprovado;
# - nota maior ou igual a 5 e menor que 7: recuperação;
# - nota menor que 5: reprovado.

nota = float(input("Digite a nota final do estudante: "))
if nota>=7:
    print("aprovado")
elif nota >= 5:
    print("recuperação")
else:
    print("reprovado")