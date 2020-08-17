from random import randint
from time import sleep
print('-=' * 20)
print('{:^40}'.format('JOGA DA MEGA SENA'))
print('-=' * 20)
lista = []
jogofull = []
quant = int(input("Quantos jogos você quer fazer? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogofull.append(lista[:])
    lista.clear()
    tot += 1
print('{:=^40}'.format(f' SORTEANDO {quant} JOGOS '))
for i, l in enumerate(jogofull):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('{:=^40}'.format(" BOA SORTE "))

