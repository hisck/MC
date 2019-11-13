import math
from math import factorial

def cos(x):
    return 1 - (x**2/math.factorial(2)) + (x**4/math.factorial(4)) - (x**6/math.factorial(6)) + (x**8/math.factorial(8)) - (x**10/math.factorial(10))

def sen(x):
    c = math.pi/2
    y = 0
    k = (x - y) // c
    newX = x - k * c

    remainder = k % 4

    if remainder == 0:
        return (x - (x**3/math.factorial(3)) + (x**5/math.factorial(5)) 
        - (x**7/math.factorial(7)) + (x**9/math.factorial(9)) 
        - (x**11/math.factorial(11)))
    elif remainder == 1:
        return cos(newX)
    elif remainder == 2:
        return - (x - (x**3/math.factorial(3)) + (x**5/math.factorial(5)) 
        - (x**7/math.factorial(7)) + (x**9/math.factorial(9)) 
        - (x**11/math.factorial(11)))
    elif remainder == 3:
        return - cos(newX)