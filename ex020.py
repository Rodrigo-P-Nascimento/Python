from random import shuffle

n1 = input("\033[31mPrimeiro aluno: ")
n2 = input("\033[32mSegundo aluno: ")
n3 = input("\033[33mTerceiro aluno: ")
n4 = input("\033[34mQuarto aluno: ")
lista = [n1, n2, n3, n4]
shuffle(lista)
print("\033[mA lista de alunos será:")
print(lista)
