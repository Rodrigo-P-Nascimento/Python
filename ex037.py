num = int(input("Digite um número inteiro: "))
print("""Escolha uma das opções abaixo para a conversão do seu valor:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opção = int(input("Digite um valor: "))
if opção == 1:
    print("\033[34mO número {} convertido é {}".format(num, bin(num)[2:]))
elif opção == 2:
    print('\033[34mO número {} convertido é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('\033[34mO número {} convetido é {}'.format(num, hex(num)[2:]))
else:
    print("\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
