# ### Atividade 12 — Comparando valores

# Crie um programa que solicite dois números e apresente os resultados das seguintes comparações:

# - os números são iguais;
# - os números são diferentes;
# - o primeiro é maior que o segundo;
# - o primeiro é menor que o segundo;
# - o primeiro é maior ou igual ao segundo;
# - o primeiro é menor ou igual ao segundo.

# Utilize f-strings para identificar cada resultado.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"Os números são iguais: {num1 == num2}")
print(f"Os números são diferentes: {num1 != num2}")
print(f"O primeiro é maior que o segundo: {num1 > num2}")
print(f"O primeiro é menor que o segundo: {num1 < num2}")
print(f"O primeiro é maior ou igual ao segundo: {num1 >= num2}")
print(f"O primeiro é menor ou igual ao segundo: {num1 <= num2}")