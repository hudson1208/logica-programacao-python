### Atividade 11 — Consulta segura

# Solicite ao usuário o nome, o e-mail e a cidade de uma pessoa 
# e armazene essas informações em um dicionário. Em seguida, solicite 
# o nome de uma chave e utilize `get()` para consultar o valor correspondente.
# Caso a chave não exista, informe que o dado não foi encontrado.

pessoa = {
    "nome": input("digite o seu nome:"),
    "email": input("digite o seu email:"),
    "cidade": input("digite o nome da cidade:")
}    

chave = input("Qual chave deseja consultar? ")

valor = pessoa.get(chave)

if valor is not None:
    print(f"{chave}: {valor}")
else:
    print("Dados nao encontrados")