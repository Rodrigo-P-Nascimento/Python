lista = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO',
        'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE',
        'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE',
        'QUINZE', 'DESESSEIS', 'DESESSETE', 'DEZOITO',
        'DEZENOVE', 'VINTE')
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    res = " "
    if 0 <= num <= 20:
        while res not in "SN":
            print(f"Você digitou o número \033[32m{lista[num]}\033[m")
            res = str(input("\033[33mVocê quer continuar [S/N]?\033[m")).strip().upper()[0]
        if res == "N":
            break
    else:
        print("\033[1:31mTente novamente!\033[m", end='')
