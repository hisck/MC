import math
from math import factorial
from math import pow

stop = 1E-11

def calculate_ln(x):
    x0 = x/2
    x1 = x + 2 * ((x - math.exp(x0))/(x + math.exp(x0)))   
    while abs(x1 - x0) > stop:
        x0 = x1
        x1 = x0 + 2 * ((x - math.exp(x0))/(x + math.exp(x0)))   
    return x1

valor = input("valor a ser calculado: ")
valor_int = float (valor)
ln_x = calculate_ln(valor_int)
print(f"PC : {math.log(valor_int, math.e)}")
print(f"A resposta é : {ln_x}")