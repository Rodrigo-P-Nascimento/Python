n = int(input("\033[1;31mDigite um número:\033[m "))
resultado = n % 2
if resultado == 0:
    print("O número é \033[4;34mPAR")
else:
    print("O número é \033[4;33mÍMPAR")

