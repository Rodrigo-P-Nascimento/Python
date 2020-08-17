sexo = str(input("Informe seu sexo: [M/F]: ").strip().upper())[0]
while sexo not in 'MF':
    sexo = str(input("\033[31mDADOS INVÁLIDOS\033[m, Por favor, informe seu sexo: ")).strip().upper()[0]
print("\033[32mSexo {} registrado no sistema com sucesso".format(sexo))