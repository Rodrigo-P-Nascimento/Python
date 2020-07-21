print("\033[30m=-" * 30)
print("\033[34mConversor de moedas, real (R$) para dólar (US$)\033[m")
print("\033[30m=-" * 30)
print("\033[mHOJE A COTAÇÃO DO DÓLAR ESTÁ R$ 3.27.")
real = float(input("Primeiro, nos diga quanto de saldo você possui e depois iremos\nlhe mostrar o seu montante em dólares.O seu saldo é de R$ "))
doll = real/3.27
print("O seu saldo em dólares será US$ \033[31m{:.2f}".format(doll))
