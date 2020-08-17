from datetime import date
ano = int(input("Qual ano você quer analisar? Coloque 0 para analisaro ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O  ano {} é \033[4;34mBISSEXTO".format(ano))
else:
    print("O ano {} não é \033[4;31mBISSEXTO".format(ano))