from time import sleep
def maior(*num):
    mai = cont = 0
    print(f"Analisando os valores: ", end='')
    for valor in num:
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
    print()
    print(f"Foram informados {cont} valores")
    print(f"O maior valor do grupo é {mai}")
    print("-" * 35)


maior(1, 2, 3, 4)
maior(3, 8, 7)
maior(6)
maior()
