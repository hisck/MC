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