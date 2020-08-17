listagem = ('Lápis', 2, 'Caderno', 10, 'Bolsa Escolar', 89.99, "Borracha", 1.50,
            'Corretivo', 3.60, 'Caneta', 1.20, 'Régua', 3, 'Tesoura', 2)
print("=" * 40)
print(f'\033[33m{"LISTA DE PREÇOS":^40}\033[m')
print("=" * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'\033[33mR${listagem[pos]:>7.2f}\033[m')
print('=' * 40)
