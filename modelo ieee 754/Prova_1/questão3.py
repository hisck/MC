from math import *
import math


def serie(x):
    res = 0
    for i in range(50):
        res = res + ((((-1)**i) * factorial(2*i)) /
                     ((1-2*i) * (factorial(i)**2) * (4**i))) * x**i
    return res


def quest_A(x):
    k = ceil(log2(x))
    x_estrela = x/(2**k)
    return (2**(k/2))*serie(x_estrela - 1)


def dec2IEEE(x):
    if x > 0:
        expoente = int(math.log(x, 2))
        mantissaReal = math.pow(2, (math.log(x, 2) - expoente))
        sinal = 1
    else:
        expoente = int(math.log(-x, 2))
        mantissaReal = math.pow(2, (math.log(-x, 2) - expoente))
        sinal = -1

    mantissaArmazenada = mantissaReal - 1

    return sinal, expoente, mantissaArmazenada, mantissaReal


def quest_B(x):
    s, e, man, m = dec2IEEE(x)
    return (2**((e+1)/2))/(2**0.5) * serie(m-1)


print(quest_A(3))
print(quest_B(3))

print(quest_A(49))
print(quest_B(49))
