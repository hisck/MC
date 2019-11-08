import math
from math import factorial
from math import pow

def calculate_ln(x):
    if x < 2:
        for i in range (1, 30):
            ln = (((pow(-1, i+1))*(pow(x - 1, i)))/i)
    else:
        for i in range (1, 30):
            ln = -(pow(-1, ( (i + 1 * (pow ( pow (x, -1) - 1, i) ) ) / i ) ) )

valor = input("valor a ser calculado: ")
valor_int = int (valor)
ln_x = calculate_ln(valor_int)
print(f"A resposta é : {ln_x}")