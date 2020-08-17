print("\033[34m{:=^30}".format(" LOJAS BÉNE "))
preço = float(input("\033[mQual o preço das suas compras: R$ "))
print("""{:^30}""".format("\033[33mFORMAS DE PAGAMENTO\033[m"))
print("""[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão""")
v = int(input("\033[33mQual o opção:\033[m "))
if v == 1:
    des = preço - preço * 10 / 100
    print("O total a pagar, com o desconto de 10%, é de R${:.2f}".format(des))
elif v == 2:
    des = preço - preço * 5 / 100
    print("O total a pagar, com o desconto de 5%, é de R${:.2f}".format(des))
elif v == 3:
    parcela = preço / 2
    print("Essa opção não oferece descontos")
    print("""Sua compra será parcelada em 2x de {:.2f}
e o valor total a ser pago é de R${:.2f}""".format(parcela, preço))
elif v == 4:
    juros = preço + preço * 20 / 100
    par = int(input("Quantas vezes? "))
    parcela = juros / par
    print("Essa opção contem juros de 20% em cima da sua compra")
    print("Sua compra será parcelada em {}x de R${}".format(par, parcela))
    print("Portanto o total a ser pago é de R${:.2f}".format(juros))
else:
    print("Porfavor tente novamente.")



