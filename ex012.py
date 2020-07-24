print("\033[36mDescontonômetro!\033[m")
pre = float(input("Qual é o preço bruto do produto? R$ "))
des = pre - (pre * 5/100)
print("O valor final do produto com desconto de 5% é de R$ {:.2f}".format(des))

