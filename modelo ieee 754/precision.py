from math import *

def cos(x)
    x = math.toRadians(ang)
    return 1 - (pow(x , 2)/factorial(2)) + (pow(x, 4)/factorial(4)) - (pow(x, 6)/factorial(6)) + (pow(x,8)/factorial(8)) - (pow(x,10)/factorial(10)) + (pow(x, 12)/factorial(12))

def sen(x):
    x = math.toRadians(ang)
    sinal = 1
    if ang > 90 && ang <= 180:
        sinal = 1
        x = pi - x
    elif ang > 180 && ang <= 270:
        sinal = -1
        x = x - pi
    elif ang > 270 && ang <= 360:
        sinal = -1
        x = 2*pi - x

    if ang <= 45:
        return (pow(x,1)/factorial(1)) - (pow(x,3)/factorial(3)) + (pow(x,5)/factorial(5)) - (pow(x,7)/factorial(7)) + (pow(x,9)/factorial(9)) - (pow(x,11)/factorial(11)) 
    else return sinal *(cos(90 - ang))


def main:
    ang = input("Angulo a ser calculado: ")
    res = sen(ang)
    print "A resposta é :"
    print(ang)
    