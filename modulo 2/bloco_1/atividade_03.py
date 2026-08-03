# ## Atividade 03 — Calculadora de IMC (decisão)

# Solicite o nome, peso e altura do usuário.

# Calcule o IMC e informe a classificação utilizando estruturas condicionais.

# Utilize a tabela oficial da OMS para definir as faixas.

# Calculadora de IMC

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"\nNome: {nome}")
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade Grau I"
elif imc < 40:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

print(f"Classificação: {classificacao}")
