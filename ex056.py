media = 0
ageoldman = 0
nameoldman = 0
cont = 0
for c in range(1, 5):
    print("\033[34m=====\033[m{}º PESSOA\033[34m=====\033[m".format(c))
    nome = str(input("NOME: ")).strip().title()
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO [M/F]: ")).strip().upper()
    print("\033[32m{}| {} anos| sexo: {}\033[m".format(nome, idade, sexo))
    media += idade
    if c == 1 and sexo == "M":
        ageoldman = idade
        nameoldman = nome
    if sexo == "M" and idade > ageoldman:
        ageoldman = idade
        nameoldman = nome
    if idade > 20 and sexo == "F":
        cont += 1
print("\033[1:33m--" * 25)
print("\033[mA média das idades do grupo é de {} anos.".format(media / c))
print("O homem mais velho do grupo é {} e ele tem {} anos.".format(nameoldman, ageoldman))
if cont == 1:
    print("E apenas uma mulher tem mais de 20 anos. ")
elif cont == 0:
    print("E nenhuma mulher no grupo tem mais de 20 anos.")
else:
    print("E {} mulheres tem mais de 20 anos.". format(cont))
