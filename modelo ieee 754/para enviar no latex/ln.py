import math
from math import factorial
from math import pow

stop = 1E-11

def calc_expoente(x):
    return math.floor(math.log(x, 2))

def plus_mantissa(x, e):
    return pow(2, (math.log(x, 2) - e))

def calculate_ln(x):
    k = calc_expoente(x)
    x0 = plus_mantissa(x, k)
    g = math.log(x0, math.e)
    ln0_x = g + (k * math.log(2, math.e))
    return ln0_x
