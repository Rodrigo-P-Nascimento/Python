n = int(input("\033[34mDigite um número para mostrar sua tabuada:\033[m "))
print('\033[33m-=' * 20)
for c in range(1, 11):
    print('\033[m{} x {:2} = {}'.format(n, c, n * c))
print('\033[33m-=' * 20)
