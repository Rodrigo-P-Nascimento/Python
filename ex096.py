def area(lar, com):
    a = lar * com
    print(f"A área de um terreno {lar} X {com} é de {a:.2f}m².")


print(" Controle de Terrenos ")
print("=" * 30)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l, c)
