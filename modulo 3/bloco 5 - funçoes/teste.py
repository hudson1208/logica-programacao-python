#  def exibir_mensagem():
#      print("Bem-vindo ao sistema.")

#  exibir_mensagem()

#  ////////////////////////////////////////////////

# def exibir_menu():
#     print("1 - Cadastrar")
#     print("2 - Consultar")
#     print("3 - Encerrar")
# exibir_menu()

#  ////////////////////////////////////////////////////

# def saudar(nome):
#     print(f"Ola, {nome}!")
# saudar("hudson gostoso e delicioso")
# saudar("caludio")

# ///////////////////////////////////////////

# def apresentar_produtor(nome, preco, estoque):
#     print(f"produtor: {nome}")
#     print(f"Preço: R${preco:.2f}")
#     print(f"Estoque: {estoque}")

# apresentar_produtor(
#     "Monitor",
#     1000.00,
#     5
# )
# /////////////////////////////////////////////////////////

# def apresentar_aluno(nome, idade, nota):
#     print(nome, idade, nota)
    
# apresentar_aluno(
#     "hudson"
#     30
#     6,5
# )

# ////////////////////////////////////
# aluno = {
#     "nota": 6.5,
#     "nome": "hudson",
#     "idade": 30
# }

# def apresentar_aluno():
#     for chave, valor in aluno.items():
#         print(f"{chave}: {valor}")

# apresentar_aluno()

# /////////////////////////////////////////////////
def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)


def classificar_aluno(media: float) -> str:
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def apresentar_resultado(notas: list[float], media: float, classificacao: str) -> None:
    print("\nResultado do aluno")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Classificação: {classificacao}")


nota1: float = float(input("Digite a primeira nota: "))
nota2: float = float(input("Digite a segunda nota: "))
nota3: float = float(input("Digite a terceira nota: "))

notas_aluno: list[float] = [nota1, nota2, nota3]

media_aluno: float = calcular_media(notas_aluno)
classificacao_aluno: str = classificar_aluno(media_aluno)

apresentar_resultado(
    notas_aluno,
    media_aluno,
    classificacao_aluno
)