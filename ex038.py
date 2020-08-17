pn = int(input("Digite um número: "))
sn = int(input("Digite o segundo número: "))
if pn > sn:
    print("O \033[31mPRIMEIRO\033[m NÚMERO É MAIOR!")
elif pn < sn:
    print("O \033[34mSEGUNDO\033[m NÚMERO É MAIOR!")
else:
    print("\033[33mOS DOIS NÚMEROS SÃO IGUAIS!")

