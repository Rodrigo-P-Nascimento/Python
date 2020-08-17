frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

"""inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]"""

print("Você digitou a frase {} e o seu inverso é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um políndromo")
else:
    print("NÃO temos um políndromo")
