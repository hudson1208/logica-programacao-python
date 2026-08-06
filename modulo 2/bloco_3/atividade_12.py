"""
# ### Atividade 12 — Pesquisa de nomes

# Cadastre inicialmente os seguintes alunos:

# ```python
# [
#     "Ana",
#     "Carlos",
#     "Maria",
#     "Pedro",
#     "Lucas"
# ]
# ```

# Solicite um nome ao usuário e informe se ele está presente na lista. Caso esteja, apresente também sua posição.
"""

alunos = [
    "Ana",
    "Carlos",
    "Maria",
    "Pedro",
    "Lucas"
]

nome = input("Digite um nome: ")

if nome in alunos:
    posicao = alunos.index(nome)
    print(f"{nome} está na lista na posição {posicao}.")
else:
    print(f"{nome} não está na lista.")   
    