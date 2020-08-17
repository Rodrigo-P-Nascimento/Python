dados = []
while True:
    nome = str(input("Nome do aluno(a): "))
    nota1 = float(input('1º nota: '))
    nota2 = float(input('2º nota: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('-=' * 15)
print(f'{"No":<4} {"NOME":<10}{"MÉDIA":>8}')
print('-=' * 15)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 35)
    opc = int(input("Deseja mostrar notas de algum aluno? (999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(dados):
        print(f'Notas do aluno {dados[opc][0]} são {dados[opc][1]}')
print("Adios....")