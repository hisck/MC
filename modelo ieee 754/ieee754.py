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

valor = input("valor a ser calculado: ")
valor_int = int (valor)
valor_expoente_calculado = calc_expoente(valor_int)
valor_mantissa_calculada = plus_mantissa(valor_int, valor_expoente_calculado)
valor_calculado = calc_valor(valor_int)
print(f"O valor da mantissa armazenada é : {valor_mantissa_calculada - 1}")
print(f"O valor da mantissa é : {valor_mantissa_calculada}")
print(f"O valor do expoente é : {valor_expoente_calculado}")
print(f"A resposta é : {valor_calculado}")