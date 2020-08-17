d = float(input("Qual a distância da sua viagem?km "))
t = d * 0.5
r = d * 0.45
if d<= 200:
    print("\033[34mO valor da sua viagem será R${:.2f}\033[m".format(t))
else:
    print("\033[31mO valor da sua viagem será R${:.2f}\033[m".format(r))

