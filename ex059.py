p1 = int(input("Digite o 1º número: "))
p2 = int(input("Digite o 2º número: "))
op = 0
while op != 5:
    print("""\033[34m======== MENU ========
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA\033[m""")
    op = int(input("Qual a sua opção: \033[32m"))
    if op == 1:
        soma = p1 + p2
        print("Soma entre {} e {} é igual a {}".format(p1, p2, soma))
    elif op == 2:
        mul = p1 * p2
        print("A multiplicação entre {} e {} é igual a {}".format(p1, p2, mul))
    elif op == 3:
        if p1 > p2:
            print("{} é o maior valor".format(p1))
        else:
            print("{} é o maior valor".format(p2))
    elif op == 4:
        p1 = int(input("Digite o 1º novo número: "))
        p2 = int(input("Digite o 2º novo número: "))
    elif op == 5:
        print("Finalizando...")
    else:
        print("\033[31mOpção invalida!\033[m Tente novamente.")
print("\033[mFim do processo!")