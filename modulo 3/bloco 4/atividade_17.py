### Atividade 17 — Remoção de cadastro

# Cadastre três estudantes em uma lista de dicionários, armazenando
# nome, idade e curso. Em seguida, solicite ao usuário o nome de um
# estudante, localize seu registro e permita removê-lo após confirmação.
# Caso o estudante não seja encontrado, informe ao usuário. Ao final,
# apresente os registros restantes.

# Cadastro dos estudantes
estudantes = [
    {"nome": "Hudson", "idade": 30, "curso": "ADS"},
    {"nome": "Maria", "idade": 22, "curso": "Direito"},
    {"nome": "João", "idade": 25, "curso": "Engenharia"}
]

nome_procurado = input("Digite o nome do estudante que deseja remover: ")

encontrado = False

for estudante in estudantes:
    if estudante["nome"].lower() == nome_procurado.lower():
        encontrado = True

        confirmacao = input(
            f"Confirma a remoção de {estudante['nome']}? (s/n): "
        ).lower()

        if confirmacao == "s":
            estudantes.remove(estudante)
            print("Estudante removido com sucesso!")
        else:
            print("Remoção cancelada.")

        break

if not encontrado:
    print("Estudante não encontrado.")


print("\nEstudantes cadastrados:")
for estudante in estudantes:
    print(estudante)