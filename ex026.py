frase = str(input("Digite uma frase qq ae: ")).strip().lower()
print("A letra A apareceu {} vezes na frase".format(frase.count("a")))
print("A primeira letra A aparece na posição {}".format(frase.find("a")+1))
print("A última letra a aparece na posição {}".format(frase.rfind("a")+1))
