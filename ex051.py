#An = a1 (n -1) . r
pt = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão: "))
décimo = pt + (10 - 1) * r
for c in range(pt, décimo + r, r):
    print('{} '.format(c), end="=> ")
print("GAME OVER")
