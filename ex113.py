def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO! Digite um valor inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("A entrade de dados foi intenrrompida pelo usuário")
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, KeyboardInterrupt, TypeError):
            print("\033[31mERRO!Digite apenas valores reais válidos.\033[m")
            continue
        else:
            return n


num = leiaInt("Digite um número inteiro: ")
flo = leiaFloat("Digite um número real: ")
print(f"O valor inteiro digitado foi {num}")
print(f"O valor real digitado foi {flo}")

