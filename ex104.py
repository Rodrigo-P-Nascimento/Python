def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else:
            print("\033[31mERRO.DIGITE APENAS VALORES INTEIROS!\033[m")
        if ok:
            break
    return valor


n = leiaInt("Digite um número: ")
print(f"Nº {n}")