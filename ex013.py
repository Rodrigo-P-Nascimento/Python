print("""\033[31mFulano ganha tanto de grana e seu patrão quis lhe dar um aumento"
de cerca de 15% em cima de seu salário.\033[m""")
s = float(input("Qual é o salário inicial do funcionário:"))
au = (s*15)/100 + s
print("""O salário de fulano depois do misterioso aumento"
passou a ser de cerca de R$ \033[1;36m{:.2f}!""".format(au))
