from math import *
import math

def calcE(x):
    n = math.ceil((x - (math.log(2, math.e)/512)*256)/math.log(2, math.e))
    r = (x - n*math.log(2))/256
    return (2**n) * (1 + r + ((r**2)/2) + ((r**3)/6) + ((r**4)/24))**256

valor = input("valor a ser calculado: ")
valor_int = float (valor)
e_x = calcE(valor)
print(f"A resposta é : {e_x}")
