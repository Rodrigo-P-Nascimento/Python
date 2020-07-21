qq = int(input("Para esse teste iremos lhe mostrar o dobro, o triplo e a raiz quadrada\nde um número de sua escolha, então diga-nos qualquer número:"))
print("Você escolheu o número {}.".format(qq))
d = qq*2
t = qq*3
rq = qq**(1/2)
print("""\033[31mDobro:\033[m{}
\033[32mTriplo:\033[m{}
\033[34mRaiz quadrada:\033[m{:.2f}""".format(d, t, rq))