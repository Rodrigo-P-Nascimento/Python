'''from math import trunc

n = float(input("Digite um número: "))
print("O número {} tem a parte inteira {}.".format(n, trunc(n)))'''

n = float(input("\033[32mDigite um número: "))
print("\033[mO número {} tem a parte inteira {}.".format(n, int(n)))