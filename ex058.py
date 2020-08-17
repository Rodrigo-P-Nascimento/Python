from random import randint
n = randint(1, 10)
cont = 1
nick = str(input("Digite o seu NICKNAME GAMER: "))
print("""\033[33mVamos ver se vc é melhor do que eu {}...
Estou pensando em um número de 1 à 10 tente adivinhar ele.\033[m""".format(nick))
palpite = int(input("Qual o seu palpite? "))
while n != palpite:
    if palpite < n:
        print("HMM...Acho que um valor MAIOR cairia melhor|")
        palpite = int(input("Qual o seu palpite: "))
        cont += 1
    else:
        print("HMM...Acho que um valor MENOR cairia melhor|")
        palpite = int(input("Qual o seu palpite: "))
        cont += 1
if cont < 3:
    print("Então {} é um mestre na adivinhação, meus PARÁBENS".format(nick))
    print("Você me venceu com {} jogada(s)".format(cont))
else:
    print("""{} você não é tão bom assim.... "
Só conseguiu me vencer com {} jogadas, mas é jogando que se aprender!""".format(nick, cont))