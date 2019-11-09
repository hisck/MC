import math
from math import factorial

def sqrtSerie(x):
    res = 0
    for i in range(100):
        res = res + ((((-1)i) * factorial(2*i)) / ((1-2*i) * (factorial(i)**2) * (4**i))) * x**i
    return res

def argumentReduction(x):
    return x/(2**k(x))


def k(x):
    return ceil(log2(x))


def g(x):
    return (2**(k(x)/2)) * (sqrtSerie(argumentReduction(x) - 1))

valor = input("valor a ser calculado: ")
valor_int = int (valor)
res = g(valor_int)
print(f"A resposta é : {res}")