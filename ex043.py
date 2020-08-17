peso = float(input("Qual o seu peso: (Kg) "))
alt = float(input("Qual a sua altura: "))
imc = peso / (alt ** 2)
if imc < 18.5:
    print("O seu IMC é de {:.1f} e você está \033[31mABAIXO DO PESO".format(imc))
elif 18.5 <= imc < 25:
    print("O seu IMC é de {:.1f} e você está no \033[32mPESO IDEAL".format(imc))
elif 25 <= imc < 30:
    print("O seu IMC é de {:.1f} e você está com \033[34mSOBREPESO".format(imc))
elif 30 <= imc < 40:
    print("O seu IMC é de {:.1f} e você está com \033[33mOBESIDADE".format(imc))
else:
    print("O seu IMC é de {:.1f} e você está com \033[31mOBESIDADE MÓRBIDA,\033[m cuidado cara!".format(imc))