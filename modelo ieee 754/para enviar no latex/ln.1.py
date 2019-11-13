import math
from math import factorial
from math import pow

def calculate_k(x):
    return math.ceil(math.log2(x))

def calculate_newX(x):
    k = calculate_k(x)
    return x/2**k

def calculate_ln(x):
    res = 0
    for i in range (1, 50):
        if i%2 == 0 :
            res = res - x**i/i
        else :
            res = res + x**i/i
    return res

def g(x):
    return (calculate_k(x)*math.log(2) + 
    (calculate_ln(calculate_newX(x) - 1)))