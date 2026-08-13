### Atividade 18 — Saudação personalizada

# Crie uma função que receba o nome de uma pessoa como parâmetro
# e apresente uma saudação personalizada. Solicite o nome ao usuário
# e utilize-o na chamada da função.

def apresentar_saudacao(nome: str) -> None:
    print(f"Olá, {nome}! Seja bem-vindo(a)!")


nome_usuario: str = input("Digite seu nome: ")

apresentar_saudacao(nome_usuario)
