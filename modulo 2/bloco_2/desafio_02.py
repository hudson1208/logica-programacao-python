# ### Desafio 02 — Caixa Registradora

# Uma loja deseja registrar várias vendas durante o dia. Desenvolva um programa que solicite o valor de cada venda e continue recebendo novos valores até que o usuário informe **0**. Ao finalizar, apresente:

# - quantidade de vendas realizadas;
# - valor total vendido;
# - valor médio das vendas;
# - maior venda registrada;
# - menor venda registrada.

# Utilize estruturas de repetição e condicionais para controlar o fluxo do programa.

quantidade_vendas = 0
total_vendido = 0
maior_venda = 0
menor_venda = 0

while True:
    venda = float(input("Digite o valor da venda ou 0 para finalizar: "))

    if venda == 0:
        break

    quantidade_vendas += 1
    total_vendido += venda

    if quantidade_vendas == 1:
        maior_venda = venda
        menor_venda = venda
    else:
        if venda > maior_venda:
            maior_venda = venda

        if venda < menor_venda:
            menor_venda = venda
        break
if quantidade_vendas > 0:
    media_vendas = total_vendido / quantidade_vendas

    print("Quantidade de vendas:", quantidade_vendas)
    print(f"Valor total vendido: R$ {total_vendido:.2f}")
    print(f"Valor médio das vendas: R$ {media_vendas:.2f}")
    print(f"Maior venda registrada: R$ {maior_venda:.2f}")
    print(f"Menor venda registrada: R$ {menor_venda:.2f}")
else:
    print("nenhum venda foi registrado")