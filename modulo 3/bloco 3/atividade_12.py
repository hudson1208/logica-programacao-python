# ### Atividade 12 — Métodos do dicionário

# Solicite ao usuário o título, o autor, o ano e a categoria de
# um livro e armazene essas informações em um dicionário. Em
# seguida, apresente todas as chaves utilizando `keys()`, todos
# os valores utilizando `values()` e todos os pares chave-valor
# utilizando `items()`. Depois, percorra o dicionário com `for`
# e `items()` para apresentar todas as informações cadastradas.

categoria = input("digite a categoria do livro: ")

livro = {
    "titulo" : titulo,
    "autor" : autor,
    "ano" : ano,
    "categoria" : categoria
}
print("\nTodas as chaves:")