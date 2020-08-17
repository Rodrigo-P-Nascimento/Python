from datetime import date
ano = date.today().year
x = int(input("Qual a data do seu nascimento: "))
idade = ano - x
if idade <= 9:
    print("Idade do atleta é {} anos, portanto sua classificação é de \033[31mMIRIN".format(idade))
elif idade <= 14:
    print("Idade do atleta é {} anos, portanto sua classificação é de \033[32mINFANTIL".format(idade))
elif idade <= 19:
    print("Idade do atleta é de {} anos, portanto sua classificação é de \033[35mJUNIOR".format(idade))
elif idade <= 25:
    print('Idade do atleta é de {} anos, portanto sua classificação é de \033[34mSÉNIOR'.format(idade))
else:
    print("Idade do atleta é de {} anos, portanto sua classificação é de \033[33mMASTER".format(idade))