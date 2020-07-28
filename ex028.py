from random import randint
from time import sleep
print("-=-" * 20)
print("MINI JOGO MERDA, FEITO PELA WENISSON SOFT")
print("-=-" * 20)
print("""O computador vai escolher um número inteiro entre 0 e 5 e
você deverá tentar acertar tal número.""")
n = randint(0, 5)
pl = int(input("Qual o seu palpite de número? "))
print('PROCESSANDO...')
sleep(3)
if n == pl:
    print("Meus parabéns, o computador digitou {} e você também!".format(n))
else:
    print("O computador digitou {} e você não conseguiu acertar, tente novamente!".format(n))
