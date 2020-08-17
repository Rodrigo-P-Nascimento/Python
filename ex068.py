from random import randint
from time import sleep
print("\033[34m=" * 40)
print('{:^40}'.format('\033[mJOGO DO PAR OU ÍMPAR'))
print("\033[34m=" * 40)
cont = 0
while True:
    jogador = int(input("\033[mDigite um número: "))
    com = randint(0, 10)
    total = com + jogador
    pi = " "
    while pi not in "PI":
        pi = str(input("Você prefere PAR ou ÍMPAR? ")).strip().upper()
        print("PROCESSANDO...")
    sleep(3)
    print(f"O jogador jogou {jogador} e o computador jogou {com}|TOTAL = {total}")
    if pi == "P":
        if total % 2 == 0:
            print("\033[33mVocê VENCEU!\033[m")
            cont += 1
        else:
            print("\033[31mVocê PERDEU!\033[m")
            break
    elif pi == "I":
        if total % 2 == 1:
            print("\033[33mVocê VENCEU!\033[m")
            cont += 1
        else:
            print("\033[31mVocê PERDEU!\033[m")
            break
    print('\033[35mVamos jogar novamente...\033[m')
    sleep(1)
print(f"\033[32mO jogador ganhou {cont} vezes.")