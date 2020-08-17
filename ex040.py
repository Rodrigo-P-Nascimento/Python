p = float(input("Digite a primeira nota: "))
s = float(input("Digite a segunda nota: "))
media = (p + s) / 2
if media >= 7.0:
    print("Sua média é de {:.1f}, você foi \033[34mAPROVADO!".format(media))
elif 5.0 <= media <= 6.9:
    print("Sua média é de {:.1f}, você está em \033[33mRECUPERAÇÃO.".format(media))
else:
    print("Sua média é de {:.1f}, você está \033[31mREPROVADO.".format(media))

