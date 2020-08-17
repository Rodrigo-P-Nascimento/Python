from datetime import date
data = int(input("Qual a sua data de nascimento: "))
idade = date.today().year - data
print("Quem nasceu em {} tem {} anos em {}".format(data, idade, date.today().year))
if idade == 18:
    print("\033[32mVocê deve ser apresentar para o seu alistamento.\033[m")
elif idade < 18:
    saldo = 18 - idade
    print("""Com a sua idade de  {} anos, ainda falta {} anos para o seu alistamento.""".format(idade, saldo))
    ano = date.today().year + saldo
    print("\033[34mO seu alistamento será em {}\033[m".format(ano))
else:
    saldo = idade - 18
    print("""Com a sua idade de {} anos, você já deveria ter se apresentado
há {} anos. Portanto trate de ser apresentar o mais rápido possível.""".format(idade, saldo))
    ano = date.today().year - saldo
    print("\033[31mVocê deveria ter se apresentado em {}.\033[m".format(ano))
