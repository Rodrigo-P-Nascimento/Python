from time import sleep
c =('\033[m',        # 0 - None
    '\033[41m', # 1 - Vermelho
    '\033[42m', # 2 - Verde
    '\033[43m', # 3 - Amarelo
    '\033[44m', # 4 - Azul
    '\033[45m', # 5 - roxo
    '\033[7;30m')     # 6 - branco


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f" {msg} ")
    print('=' * tam)
    print(c[0], end='')
    sleep(2)


def ajuda(msg):
    titulo(f"Acessando o manual do comando...")
    print(c[6], end='')
    help(msg)
    print(c[0], end='')
    sleep(2)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA ROD2000', 4)
    comando = str(input("Digite o comando para saber o manual: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)