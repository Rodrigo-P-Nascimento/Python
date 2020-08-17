salario = float(input("Qual o seu salário:R$ "))
if salario <= 1250.00:
    salario1 = (salario * 15) / 100 + salario
else:
    salario1 = (salario * 10) / 100 + salario
print("O seu salário era de R$\033[36m{:.2f}\033[m e agora será de R$\033[33m{:.2f}".format(salario, salario1))
