# ## Atividade 18 — Conversor de temperatura

# Solicite uma temperatura em graus Celsius e converta para Fahrenheit.

# Fórmula:

# ```
# fahrenheit = celsius * 1.8 + 32
# ```

# Apresente o resultado com duas casas decimais.

celsius= float(input("Digite a temperatura em graus Celsius:")  )
fahrenheit = celsius * 1.8 + 32

print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")