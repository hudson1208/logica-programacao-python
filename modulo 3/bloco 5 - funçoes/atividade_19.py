# ### Atividade 19 — Operações matemáticas

# Crie funções separadas para somar, subtrair, multiplicar e dividir dois números.
# Cada função deverá receber os números como parâmetros e retornar o resultado da
# operação. Solicite os valores ao usuário e utilize as funções para realizar os
# cálculos. Na divisão, trate a tentativa de divisão por zero.

def somar(numero1: float, numero2: float) -> float:
    return numero1 + numero2


def subtrair(numero1: float, numero2: float) -> float:
    return numero1 - numero2


def multiplicar(numero1: float, numero2: float) -> float:
    return numero1 * numero2


def dividir(numero1: float, numero2: float) -> float | None:
    if numero2 == 0:
        return None

    return numero1 / numero2


numero1: float = float(input("Digite o primeiro número: "))
numero2: float = float(input("Digite o segundo número: "))

print(f"Soma: {somar(numero1, numero2)}")
print(f"Subtração: {subtrair(numero1, numero2)}")
print(f"Multiplicação: {multiplicar(numero1, numero2)}")

resultado_divisao: float | None = dividir(numero1, numero2)

if resultado_divisao is None:
    print("Divisão: não é possível dividir por zero.")
else:
    print(f"Divisão: {resultado_divisao}")