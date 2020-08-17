print("\033[34m=-=\033[m" * 20)
print("\033[33mANALISADOR DE TRIÂNGULOS\033[m")
print("\033[34m=-=\033[m" * 20)

r1 = float(input("Digite o primeiro valor: "))
r2 = float(input("Digite o segundo valor: "))
r3 = float(input("Digite o terceiro valor: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\033[32mSIM! Estes valores podem formar um triângulo")
else:
    print("\033[31mNÃO! Estes valores não conseguem formar um triângulo")

