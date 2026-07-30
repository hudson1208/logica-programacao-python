# # Atividade 06 — Contagem Regressiva

# Solicite um número inteiro ao usuário e apresente a contagem regressiva até zero.

# Exemplo:

# ```
# 5
# 4
# 3
# 2
# 1
# 0

# Solicita um número inteiro

numero = int(input("Digite um número inteiro: "))
for i in range(numero, -1, -1):

    print(i)