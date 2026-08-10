### Atividade 09 — Cadastro de pessoa

# Solicite ao usuário o nome, a idade, a cidade e a profissão de uma pessoa. Armazene essas informações em um 
# dicionário e, ao final, apresente cada dado utilizando sua respectiva chave.

# Cadastro de pessoa

# Cadastro de pessoa

pessoa = {}

pessoa["nome"] = input("Digite o nome da pessoa: ")
pessoa["idade"] = int(input("Digite a idade da pessoa: "))
pessoa["cidade"] = input("Digite a cidade da pessoa: ")
pessoa["profissao"] = input("Digite a profissão da pessoa: ")

print("\n--- Dados da pessoa cadastrada ---")
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
print("Profissão:", pessoa["profissao"])

