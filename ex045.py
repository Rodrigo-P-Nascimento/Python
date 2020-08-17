from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""\033[33mSuas opções:\033[m
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input("\033[33mQual a sua jogada?\033[m "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("POOO!!!!")
print("\033[34m-=" * 20)
print("\033[mComputador jogou \033[31m{}\033[m".format(itens[computador]))
print("Jogador jogou \033[35m{}\033[m".format(itens[jogador]))
print("\033[34m-=\033[m" * 20)
if computador == 0: #PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("\033[32mJOGADOR VENCEU!")
    elif jogador == 2:
        print("\033[31mCOMPUTADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1: #PAPEL
    if jogador == 0:
        print("\033[31mCOMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("\033[32mJOGADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2: #TESOURA
    if jogador == 0:
        print("\033[32mJOGADOR VENCEU")
    elif jogador == 1:
        print("\033[31mCOMPUTADOR VENCEU!")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")
