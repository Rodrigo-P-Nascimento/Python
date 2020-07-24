from math import radians, sin, cos, tan
n = float(input("Qual o ângulo você deseja saber os valores: "))
c = cos(radians(n))
s = sin(radians(n))
t = tan(radians(n))
print("\033[31mO ângulo de {} tem COSSENO {:.2f}".format(n, c))
print("\033[34mO ângulo de {} tem SENO {:.2f}".format(n, s))
print("\033[35mO ângulo de {} tem TANGENTE {:.2f}".format(n, t))
