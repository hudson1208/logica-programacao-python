# ### Atividade 11 — Calculadora básica

# Crie um programa que solicite dois números e apresente:

# - soma;
# - subtração;
# - multiplicação;
# - divisão;
# - divisão inteira;
# - resto da divisão;
# - potência.

# Converta as entradas corretamente e utilize f-strings para exibir os resultados.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"\nSoma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
print(f"Divisão: {num1 / num2}")
print(f"Divisão inteira: {num1 // num2}")
print(f"Resto da divisão: {num1 % num2}")
print(f"Potência: {num1 ** num2}")
    
