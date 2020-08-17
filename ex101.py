def voto():
    """
    -> Essa função serve para saber qual é o tipo de voto de uma pessoa.
    Ex. Se a idade é abaixo de 16 anos, não há a possibilidade de voto.
        Se a idade é entre 16, 17 e acima de 65 anos, o voto é opicional.
        Se a idade é acima de 18 anos e menor que 65, o voto é obrigatório.
    :return:
    """
    from datetime import date
    nas = int(input("Qual ano você nasceu: "))
    idade = date.today().year - nas
    print(f"A sua idade atual é de {idade} anos, e o seu voto é ", end='')
    if idade < 16:
        print('NÃO OBRIGATÓRIO')
    elif 18 <= idade <= 65:
        print('OBRIGATÓRIO')
    elif 16 <= idade <= 17 or idade > 65:
        print("OPICIONAL")


voto()
help(voto)

