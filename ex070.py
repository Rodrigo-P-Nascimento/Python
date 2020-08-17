print('\033[34m=' * 30)
print('{:^30}'.format( 'LOJA BARATÂO 2000' ))
print('\033[34m=' * 30)
soma = cont = m = contm = 0
cheap = ' '
while True:
    nome = str(input("\033[mDigite o nome do produto: ")).strip().title()
    preço = float(input("Digite o preço do produto: R$ "))
    contm += 1
    soma += preço
    if preço > 1000:
        cont += 1
    if contm == 1 or preço < m:
        m = preço
        cheap = nome
    resposta = ' '
    while resposta not in "SN":
        resposta = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if resposta == "N":
        break
print('\033[34m-=' * 30)
print(f"\033[mA soma total que deverá ser paga é de R${soma:.2f}")
print(f"{cont} produtos custam mais de R$ 1000.00 ")
print("O produto mais barato foi {} que custa R${:.2f}".format(cheap, m))


