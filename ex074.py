from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print("Valores sorteados: ", end='')
for n in num:
    print(f'{n}', end=' ')
print(' ')
print('\033[37m=' * 30)
print(f'\033[mO maior valor foi {max(num)}')
print(f'O menor valor foi {min(num)}')
cont = menor = maior = 0
for n in num:
    cont += 1
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'{maior} , {menor}')
