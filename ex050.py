"""from random import randint
soma = 0
cont = 0
print("-=" * 20)
for c in range(1, 7):
    n = randint(1, 100)
    print(n)
    if n % 2 == 0:
        soma += n
        cont += 1
print("-=" * 20)
if cont ==1 :
    print("Na seleção automatica do PC teve {} número PAR, na qual é o valor {}".format(cont, soma))
else:
    print("Na seleção automatica do PC teve {} PARES e a soma entre eles é de {}".format(cont, soma))"""

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input("Digite o {}º número:".format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print("Você digitou {} PARES e a soma entre eles é de {}".format(cont, soma))