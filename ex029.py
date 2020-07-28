vel = float(input("Qual a sua velocidade? "))
mul = (vel - 80) * 7
if vel <= 80:
    print("Velocidae esta dentro dos padrões.")
else:
    print("""Você esta a {} km/h, que está acima do limite permitido."
Sua multa será de R${}.""".format(vel, mul))
print("Tenha um bom dia, dirija com segurança!")