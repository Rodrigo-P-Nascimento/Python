cont = mulher = homem = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    p = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if idade >= 18:
        cont += 1
    if sexo == "M":
        homem += 1
    elif sexo == "F" and idade >= 20:
        mulher += 1
    while p not in "SN":
        p = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if p == 'N':
            break
print(f'Ao todo temos {cont} pessoas que tem mais de 18 anos;')
print(f"Ao todo temos {homem} homens cadastrados;")
print(f"Total de {mulher} mulheres tem mais de 20 anos")

