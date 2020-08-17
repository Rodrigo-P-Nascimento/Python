lista = list()
menor = maior = 0
for c in range(0, 5):
    lista.append(int(input(f"Digite o {c + 1}º número na posição {c}: ")))
    if c == 0:
        menor = maior = lista[c]
    else:
        if lista[c] < menor:
            menor = lista[c]
        if lista[c] > maior:
            maior = lista[c]
print(f'O menor valor foi o nº {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}", end=' ')
print()
print(f'O maior valor foi o nº {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}', end=' ')
