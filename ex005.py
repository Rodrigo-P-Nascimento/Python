#n = int(input('Escreva um número para que seja lhe dado o valor de seu antecessor e sucessor:'))
#print('O seu número é {}'.format(n))
#at = n - 1
#su = n + 1
#print('Antecessor dele é {} e seu sucessor é {}!'.format(at,su))
n = int(input('\033[33mEscreva um número para que seja lhe dado o valor de seu antecessor e sucessor: \033[m'))
print('O seu número é {}'.format(n))
print('Antecessor dele é \033[35m{}\033[m e seu sucessor é \033[36m{}\033[m!'.format((n-1), (n+1)))
