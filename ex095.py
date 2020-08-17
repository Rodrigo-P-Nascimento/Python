time = list()
dados = dict()
partidas = list()
while True:
    dados.clear()
    dados['nome'] = str(input("Nome do jogador: ")).title()
    quant = int(input(f"Quantas partidas {dados['nome']} jogou: "))
    partidas.clear()
    for c in range(1, quant + 1):
        dados['gols'] = int(input(f"   ->Na {c}º partida quantos gols ele fez: "))
        partidas.append(dados['gols'])
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        res = str(input("Quer continuar [S/N]: ")).upper()[0]
        if res in 'SN':
            break
        print("ERRO! Responda apenas com S ou N.")
    if res == "N":
        break
print('=' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=' * 30)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERROR! Não exite jogador com ese código.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
    for i, g in enumerate(time[busca]['gols']):
        print(f'   No jogo {i + 1} fez {g} gols. ')
    print('-' * 40)
print('VOLTE SEMPRE MEU CONSAGRADO!!!')

