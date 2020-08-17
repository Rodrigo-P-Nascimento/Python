lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado, não será adicionado.")
    res = ' '
    while res not in "SN":
        res = str(input("Deseja continuar [S/N]:")).strip().upper()[0]
    if res == "N":
        break
print("Os seus valores são ", end='')
print(sorted(lista))