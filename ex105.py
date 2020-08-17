def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = "Boa"
        elif r['média'] >= 5:
            r['situação'] = "Razoável"
        elif r['média'] < 5:
            r['situação'] = "Ruim"
    for k, v in r.items():
        print(f'{k} ', end='= ')
        print(f'{v}')
    return r


#Programa princinpal

resp = notas(6, 1.2, 3, 4, sit=True)
print(resp)