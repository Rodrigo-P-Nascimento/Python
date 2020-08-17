maior = 0
menor = 0
for n in range(1, 6):
    peso = float(input("Qual é o peso da {}º pessoa:Kg ".format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso foi de {}Kg".format(maior))
print("O menor peso foi de {}Kg".format(menor))

