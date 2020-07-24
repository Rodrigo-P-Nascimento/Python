from math import hypot
'''cop = float(input("Qual o comprimento do cateto oposto: "))
cad = float(input("Qual o comprimento do cateto adjacente: "))
hi = (cop ** 2 + cad ** 2) ** (1/2)
print("A hipotenusa será {}.".format(hi))'''

cop = float(input("Qual o comprimento do cateto oposto: "))
cad = float(input("Qual o comprimento do cateto adjacente: "))
hi = hypot(cop, cad)
print("A hipotenusa será \033[33m{:.2f}".format(hi))

