import moeda

num = float(input("Digite o preço: R$ "))
print(f'O valor {num} aumentado 10% é {moeda.aumentar(num, 10):.2f}')
print(f'O valor {num} diminuido 15% é {moeda.diminuir(num, 15):.2f}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
