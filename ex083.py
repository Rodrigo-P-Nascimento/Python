# VALIDAÇÃO DE EXPRESSÕES MATEMATICAS
expre = str(input("Digite a sua expressão: "))
lista = []
for cada in expre:
    if cada == '(':
        lista.append('(')
    elif cada == ')':
        lista.append(')')
if len(lista) % 2 == 0:
    print("Essa expressão está correta ")
else:
    print("Essa expressão está incorreta")