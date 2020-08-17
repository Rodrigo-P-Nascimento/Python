from random import randint
from time import sleep
from operator import itemgetter
resl = {}
for c in range(1, 5):
    resl[f'Jogador {c}'] = randint(1, 6)
ranking = {}
print("-=-" * 15)
print(f'{"JOGO DE DADOS":^45}')
print("-=-" * 15)
print(f'{"Valores sorteados":^45}')
for k, v in resl.items():
    print(f"O {k} tirou no dado o número {v}")
    sleep(1)
print('-=-' * 15)
print(f'{"RANKING":^45}')
print('-=-' * 15)
ranking = sorted(resl.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: O {v[0]} com {v[1]} no dado')
    sleep(1)