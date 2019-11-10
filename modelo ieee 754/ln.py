import math
from math import factorial
from math import pow
from ieee754 import *

stop = 1E-11

def calculate_ln(x):
    k = calc_expoente(x)
    x0 = plus_mantissa(x, k) - 1
    g = math.log(x0, math.e)
    ln0_x = g + (k * math.log(2, math.e))
    return ln0_x

valor = input("valor a ser calculado: ")
valor_int = float (valor)
ln_x = calculate_ln(valor_int)
print(f"PC : {math.log(valor_int, math.e)}")
print(f"A resposta é : {ln_x}")