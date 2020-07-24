dias = int(input("Quantos dias esse carro foi alugado? "))
km = float(input("Quantos km foram rodados? "))
preco = (dias * 60) + (km * 0.15)
print("""Com \033[35m{}\033[m dias de uso e \033[36m{}\033[m km
rodados o valor a ser pago deverá ser de R${:.2f}.""".format(dias, km, preco))
