pt = int(input("Primeiro termo da PA: "))
razão = int(input("Razão: "))
termo = pt
cont = 0
while cont <= 10:
    print("{} > ".format(termo), end="")
    termo += razão
    cont += 1
print("FIM")