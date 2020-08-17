listafull = []
listapar = []
listaimpar = []
while True:
    listafull.append(int(input("Digite um número: ")))
    res = ' '
    while res not in "SN":
        res = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if res == 'N':
        break
for c in listafull:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print('=' * 30)
print(f'A lista completa é {sorted(listafull)}')
print(f'Os valores da lista que são pares são {sorted(listapar)}')
print(f'Já os valores que são ímpares são {sorted(listaimpar)}')