# ### Atividade 09 — Login do sistema

# Crie um programa que continue solicitando usuário e senha até que os valores estejam corretos.

# Considere:

# ```python
# usuario = "admin"
# senha = "python123"
# ```

# Ao final, apresente uma mensagem de acesso autorizado.

usuario = input("digite o usuario: ")
senha = input("digite a senha: ")

while usuario != "admin" or senha != "python123":
    print("usuario ou senha incorreta, tente novamente. ")
   
    usuario = input("digite o usuario: ")
    senha = input("digite a senha: ")


print("login correto")






















   