print("\033[36mQUANTO DE TINTA VC PRECISA PARA PINTAR AQUELA SUA PAREDE,VERSÃO 2.0\033[m")
lar = float(input("Quanto é a largura da sua parede, em metros?"))
com = float(input("Quanto é o comprimento da sua parede, em metros?"))
are = lar * com
f = are/2
print("""Bem, cada litro de tinta cobre exatamento 2m² da parede, então pelas medidas fornecidas
você precisará de \033[1;35m{:.2f}\033[m L de tinta para preencher toda a área da sua parede.""".format(f))
