cont = soma = maior = menor =  0
letra = "S"
while letra in "Ss":
    n = int(input("Digite um número: "))
    cont += 1
    letra = str(input("Quer continuar [S/N]: ")).upper().strip()[0]
    soma += n
    if cont == 1:
         maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print("Foi digitado {} valores, a média foi de {:.2f}".format(cont, media))
print("O maior valor foi {} e menor foi {}".format(maior, menor))