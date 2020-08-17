from random import randint
from time import sleep
lista = list()
soma = 0


def sorteio():
    print(f'Os 5 valores sorteados foram: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print()


def somaPar():
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f"A soma de todos os números pares é {soma}")


sorteio()
somaPar()