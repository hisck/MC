import math
from math import factorial

# def cos(x):
    # return 1 - (x**2/factorial(2)) + (x**4/factorial(4)) - (x**6/factorial(6)) + (x**8/factorial(8)) - (x**10/factorial(10)) + (x**12/factorial(12))

# def sen(x):
    # x0 = math.radians(x)
    # c = math.pi/2
    # y = 0
    # k = (x0-y)//c
    # x1 = x0 - k * c

    # quadrante = k % 4
    # if (quadrante == 0):
        # return (x0 - (x0**3/math.factorial(3)) + (x0**5/math.factorial(5)) - (x0**7/math.factorial(7)) + (x0**9/math.factorial(9)) - (x0**11/math.factorial(11)))
    # elif (quadrante == 1):
        # return cos(x1)
    # elif (quadrante == 2):
        # return - (x0 - (x0**3/math.factorial(3)) + (x0**5/math.factorial(5)) - (x0**7/math.factorial(7)) + (x0**9/math.factorial(9)) - (x0**11/math.factorial(11)))
    # elif (quadrante == 3):
        # return - cos(x1)

def cos(x):
    return 1 - (x**2/math.factorial(2)) + (x**4/math.factorial(4)) - (x**6/math.factorial(6)) + (x**8/math.factorial(8)) - (x**10/math.factorial(10))

def sen(x):
    c = math.pi/2
    y = 0
    k = (x - y) // c
    newX = x - k * c

    remainder = k % 4

    if remainder == 0:
        return (x - (x**3/math.factorial(3)) + (x**5/math.factorial(5)) - (x**7/math.factorial(7)) + (x**9/math.factorial(9)) - (x**11/math.factorial(11)))
    elif remainder == 1:
        return cos(newX)
    elif remainder == 2:
        return - (x - (x**3/math.factorial(3)) + (x**5/math.factorial(5)) - (x**7/math.factorial(7)) + (x**9/math.factorial(9)) - (x**11/math.factorial(11)))
    elif remainder == 3:
        return - cos(newX)

ang = input("Angulo a ser calculado: ")
ang = float (ang)
x = math.radians(ang)
res = sen(x)
print(f"A resposta é : {res}")
print(f"PC : {math.sin(x)}")