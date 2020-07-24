print("\033[32m=-=" * 20)
print("\033[33mConversor de temperatura!")
print("\033[32m=-=" * 20)
c = float(input("\033[mQual é a temperatura? ºC "))
k = c + 273
f = 1.8 * c + 32
print('\033[mA sua temperatura em Celsius é {}, em Kelvin é {} e em Fahrenhit é {}.'.format(c, k, f))
