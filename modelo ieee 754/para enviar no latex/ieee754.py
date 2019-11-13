import math
from math import log
from math import floor
from math import pow

def calc_expoente(x):
    return floor(log(x, 2))

def plus_mantissa(x, e):
    return pow(2, (log(x, 2) - e))

def calc_valor(x):
    signal = 1
    if x < 0:
        signal = -1
    else :
        signal = 1
    expoente = calc_expoente(x)
    mantissa = plus_mantissa(x, expoente)
    return signal * mantissa * pow(2, expoente)