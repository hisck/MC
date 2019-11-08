import math
from math import factorial
from math import pow

def exp(x):
    c = math.log(2, math.e)
    k = math.ceil( ( (c - x) / ( -c) ) )
    xk = x - (k * c)
    valor_calc = calculate_ex(xk)
    return 2**k * valor_calc

def calculate_ex(x):
    ex = 1
    for i in range (1, 17):
        ex = ex + ((pow(x, i)/factorial(i)))
    return ex

valor = input("valor a ser calculado: ")
valor_int = int (valor)
e_x = calculate_ex(valor_int)
print(f"A resposta é : {e_x}")
print(f"PC : {math.exp(valor_int)}")