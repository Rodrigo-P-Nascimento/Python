casa = float(input("Qual o valor da casa: R$"))
salario = float(input("Quanto você recebe de salário: R$"))
time = int(input("Em quantos anos você pretende pagar o financiamento? "))
fina = casa / (time * 12)
if fina >= (salario * 30 / 100):
    print("""Infelizmente o seu financiamento foi \033[31mNEGADO\033[m, 
pois as parcelas serão de R${:.2f} e você não pode pagar dentro do prazo
de {} anos""".format(fina, time))
else:
    print("""Parabéns, o seu financiamento foi \033[32mAPROVADO\033[m,"
suas parcelas serão de R${:.2f},por {} anos""".format(fina, time))
