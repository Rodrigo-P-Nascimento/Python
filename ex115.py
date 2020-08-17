import modulosss
from time import sleep
#from ex113 import leiaInt

arq = "cursoemvideo.txt"

if not modulosss.arquivoExiste(arq):
    modulosss.criarArquivo(arq)


while True:
    resp = modulosss.menu(['Ver lista de pessoas', 'Cadastrar uma nova pessoa', 'Sair do programa'])
    if resp == 1:
        modulosss.lerArquivo(arq)
    elif resp == 2:
        modulosss.cabeçalho("Novo Cadastro")
        nome = str(input("Nome: ")).strip().title()
        idade = int(input("Idade: "))
        modulosss.cadastrar(arq, nome, idade)
    elif resp == 3:
        modulosss.cabeçalho('Obrigado por usar nosso programa!')
        break
    else:
        print("\033[31mERRO! Opção inválida\033[m")
        sleep(2)


