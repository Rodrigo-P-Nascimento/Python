from datetime import date
data = date.today().year
cont = 0
cont1 = 0
for c in range(1, 8):
    nasci = int(input("Em que ano a {}º pessoa nasceu? ".format(c)))
    idade = data - nasci
    if idade >= 21:
        cont = cont + 1
    else:
        cont1 = c - cont
print("{} pessoas já são maiores de idade".format(cont))
print("{} pessoas ainda são menores de idade".format(cont1))


