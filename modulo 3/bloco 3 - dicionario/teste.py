# alunos = [
#     {
#         "nome": "Ana",
#         "idade": 18,
#         "nota": 8.5
#     },
#     {
#         "nome": "Carlos",
#         "idade": 19,
#         "nota": 7.0
#     }
# ]

# print(alunos[1]["nome"])
# //////////////////////////////////////////////

# Cadastro da pessoa
pessoa = {
    "nome": input("Digite o nome: "),
    "email": input("Digite o e-mail: "),
    "cidade": input("Digite a cidade: ")
}

# Consulta de uma chave
chave = input("Qual chave deseja consultar? ")

valor = pessoa.get(chave)

if valor is not None:
    print(f"{chave}: {valor}")
else:
    print("Dado não encontrado.")