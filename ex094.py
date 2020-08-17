dados = dict()
lista = list()
cont = soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input("Nome: ")).strip().title()
    dados['idade'] = int(input('Idade: '))
    while True:
        dados['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
        if dados['sexo'] in "MF":
            break
        print("ERRO! Por favor digite somente F ou M.")
    cont += 1
    soma += dados['idade']
    lista.append(dados.copy())
    while True:
        res = str(input("Deseja continuar [S/N]: ")).upper()[0]
        if res in 'SN':
            break
        print("ERRO! Somente é permetido S ou N.")
    if res == "N":
        break
print('-=' * 20)
print(f"{len(lista)} pessoas foram cadatradas.")
media = soma / len(lista)
print(f'A média de idade é {media:5.2f} anos.')
print(f'As mulheres cadatradas foram: ', end='')
for p in lista:
    if p['sexo'] in "F":
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print(f'{p["nome"]}')
print('<<< ENCERRANDO >>>')