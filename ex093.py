dados = dict()
partidas = list()
dados['nome'] = str(input("Nome do jogador: ")).title()
quant = int(input("Quantas partidas ele jogou: "))
for c in range(1, quant + 1):
    dados['gols'] = int(input(f"   ->Na {c}º partida quantos gols ele fez: "))
    partidas.append(dados['gols'])
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('=' * 30)
print(dados)
print('=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 30)
print(f'O jagador {dados["nome"]} jogou {quant} partidas.')
for p, g in enumerate(partidas):
    print(f'   =>Na partida {p + 1}, fez {g} gols.')
print(f"Um total de {dados['total']} de gols")