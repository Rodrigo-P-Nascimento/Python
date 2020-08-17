listagem = ("PYTHON", 'VACA', 'PAÇOCA', 'XADREZ', 'CANADÁ', 'ARTICO',
            'MINECRAFT', 'YOUTUBE', 'WENISSON', 'RODRIGO')
for p in listagem:
    print(f"\nNa palavra \033[31m{p:9}\033[m temos as vogais: ", end='')
    for letra in p:
        if letra in "AÁÂÃÀEÉÊIOÕU":
            print(f'\033[31m{letra.lower()}\033[m', end=' ')


