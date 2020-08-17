lista = (int(input("Digite o 1º número: ")),
         int(input("Digite o 2º número: ")),
         int(input("Digite o 3º número: ")),
         int(input("Digite o 4º número: ")))
print(f"Você digitou os seguinte valores:\033[34m {lista}")
print(f'\033[mO valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O primeiro valor 3 foi digitado na {lista.index(3) + 1}º posição')
else:
    print("O valor 3 não foi listado")
print("Os valores pares foram: ", end='')
for j in lista:
    if j % 2 == 0:
        print(j, end=' ')


