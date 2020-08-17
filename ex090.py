ficha = dict()
ficha['Nome'] = str(input('Nome do aluno: ')).title()
ficha['Media'] = float(input(f'Média do aluno {ficha["Nome"]}: '))
if ficha['Media'] >= 7:
    ficha['Situação'] = "APROVADO"
elif 5 <= ficha['Media'] < 7:
    ficha['Situação'] = 'RECUPERAÇÃO'
else:
    ficha['Situação'] = "REPROVADO"
print('-=' * 15)
for k, v in ficha.items():
    print(f'>\033[34m  {k} \033[mé igual a {v}')

