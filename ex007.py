print("\033[36mPara calcular a média do aluno basta digitar as duas notas do mesmo.\033[m")
n1 = float(input('1º nota: '))
n2 = float(input('2º nota: '))
media = (n1+n2)/2
print('A média do aluno é {:.1f}'.format(media))
