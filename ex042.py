lado1 = float(input("Digite um número: "))
lado2 = float(input("Digite o segundo número: "))
lado3 = float(input("Digite o terceiro número: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("\033[32mEstes valores podem formar um triângulo", end=" ")
    if lado1 == lado2 == lado3:
        print("EQUILÁTERO!")
    elif lado1 != lado2 != lado3 != lado1:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")

else:
    print("\033[31mEstes valores NÃO podem formar um trinângulo.\033[m")
