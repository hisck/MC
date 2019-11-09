import math
from math import fabs
stop = 1E-11

def calculatesqrt(x):
    x0 = x/2
    x1 = ((1/2)*(x0 + (x/x0)))
    while abs(x1-x0) > stop:
        x0 = x1
        x1 = ((1/2)*(x0 + (x/x0)))
    return x1

valor = input("valor a ser calculado: ")
valor_int = int (valor)
res = calculatesqrt(valor_int)
print(f"A resposta é : {res}")