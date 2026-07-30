# # Atividade 07 — Tabuada

# Solicite um número inteiro e apresente sua tabuada de 1 até 10 utilizando um laço de repetição.

# Exemplo:

# ```
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70


numero = int(input("Digite um número inteiro: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")