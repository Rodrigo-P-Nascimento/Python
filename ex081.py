lista = list()
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    res = ' '
    while res not in "SN":
        res = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if res == "N":
        break
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f"O valor 5 se encontra na lista na {lista.index(5) + 1}º posição")
else:
    print("O valor 5 não se encontra na lista")

