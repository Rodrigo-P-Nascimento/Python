from datetime import date

dados = dict()
dados['nome'] = str(input("Nome: ")).title()
nas = int(input("Ano de nascimento: "))
dados['CTPS'] = int(input("Nº da Carteira de trabalho (0 em caso de não ter): "))
dados['idade'] = date.today().year - nas
if dados['CTPS'] != 0:
    dados['contratação'] = int(input("Ano da contratação: "))
    dados['salario'] = int(input("Salário:R$ "))
    dados['aposentadoria'] = (dados['contratação'] + 35) - nas
print('-=' * 25)
for k, v in dados.items():
    print(f'  > {k} tem o valor {v}')
