# ### Atividade 13 — Remoção de dados

# Solicite ao usuário os dados de um funcionário, como nome, cargo,
# setor e salário, e armazene essas informações em um dicionário.
# Em seguida, solicite o nome de uma chave que deseja remover,
# verifique se ela existe e realize a remoção. Caso a chave não exista,
# informe ao usuário. Ao final, apresente o cadastro atualizado.

funcionario = {}

funcionario["nome"] = input("Digite o nome do funcionário: ")
funcionario["cargo"] = input("Digite o cargo do funcionário: ")
funcionario["setor"] = input("Digite o setor do funcionário: ")
funcionario["salario"] = float(input("Digite o salário do funcionário: R$ "))

chave = input("\nDigite o nome da chave que deseja remover: ")

if chave in funcionario:
    funcionario.pop(chave)
    print(f"\nA chave '{chave}' foi removida com sucesso.")
else:
    print(f"\nA chave '{chave}' não existe no cadastro.")

print("\n--- Cadastro atualizado do funcionário ---")

for chave, valor in funcionario.items():
    if chave == "salario":
        print(f"{chave}: R$ {valor:.2f}")
    else:
        print(f"{chave}: {valor}")