import math
from math import factorial

def cos(x):
    x = math.radians(int (ang))
    return 1 - (pow(x , 2)/factorial(2)) + (pow(x, 4)/factorial(4)) - (pow(x, 6)/factorial(6)) + (pow(x,8)/factorial(8)) - (pow(x,10)/factorial(10)) + (pow(x, 12)/factorial(12))

def sen(x):
    x = math.radians(int (ang))
    sinal = 1
    if (int (ang)) > 90 and (int (ang)) <= 180:
        sinal = -1
        x = math.pi - x
    elif (int (ang)) > 180 and (int (ang)) <= 270:
        sinal = -1
        x = x - math.pi
    elif (int (ang)) > 270 and (int (ang)) <= 360:
        sinal = 1
        x = 2*math.pi - x

    if (int (ang)) <= 45:
        return (pow(x,1)/factorial(1)) - (pow(x,3)/factorial(3)) + (pow(x,5)/factorial(5)) - (pow(x,7)/factorial(7)) + (pow(x,9)/factorial(9)) - (pow(x,11)/factorial(11)) 
    else:
        return sinal *(cos(90 - (int (ang))))

ang = input("Angulo a ser calculado: ")
res = sen(ang)
print(f"A resposta é : {res}")
    