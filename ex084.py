lista = list()
cont = maiorpeso = menorpeso = 0
while True:
    n = str(input("Nome: "))
    lista.append(n)
    p = float(input("Peso: "))
    lista.append(p)
    cont += 1
    if cont == 1:
        maiorpeso = menorpeso = p
    elif p < menorpeso:
        menorpeso = p
    elif p > maiorpeso:
        maiorpeso = p
    res = ' '
    while res not in 'SN':
        res = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if res == 'N':
        break
print("=" * 30)
print(f"Foram cadatradas {cont} pessoas")
print(f'Maior peso foi de {maiorpeso} kg, que é o peso de ', end='')
for v, c in enumerate(lista):
    if c == maiorpeso:
        print(f'{lista[v - 1]}', end='|')
print()
print(f'O menor peso foi de {menorpeso} kg, que é o peso de ', end='')
for v, c in enumerate(lista):
    if c == menorpeso:
        print(f'{lista[v - 1]}', end='|')

