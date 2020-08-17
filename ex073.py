times = 'Flamengo',	'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',\
        'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco',\
        'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',	\
        'Chapecoense', 'Avaí'
print('=' * 30)
for t in times:
    print(t)
print('=' * 30)
print(f'Os 5 primeiros times são \033[34m{times[0:5]}\033[m')
print('=' * 30)
print(f"Os 4 últimos foram {times[-4:]}")
print('=' * 30)
print(f'Os time em ordem alfabética é {sorted(times)}')
print('=' * 30)
print(f"A posição da Chapecoense é {times.index('Chapecoense') + 1}º posição")
print('=' * 30)