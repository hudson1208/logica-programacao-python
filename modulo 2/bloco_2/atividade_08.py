# Solicite ao usuário um número inteiro positivo.

# Calcule a soma de todos os números entre **1** e o valor informado.

# Exemplo:

# ```
# Entrada:
# 5

# Saída:
# 15

numero = int(input("digite um número inteiro positivo: "))

soma = 0

for i in range(1, numero + 1):

    soma += i

print("A soma é:", soma)

