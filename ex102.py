def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número inteiro.
    Com a opção de mostrar o calcúlo ou não.
    :param n: Número a ser mostrado o fatorial
    :param show: Se vai ser mostrado o calcúlo ou não
    :return:
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(4, True))