num = [[], []]
for c in range(0, 7):
    n = int(input(f"Digite o {c + 1}º número: "))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print('=' * 30)
print(f'Os valores pares digitados foram:\033[34m {sorted(num[0])}')
print(f'\033[mJá os valores ímpares digitados foram:\033[33m {sorted(num[1])}')


