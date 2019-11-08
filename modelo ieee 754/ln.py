import math
from math import factorial
from math import pow

def calculate_ln(x):
    return ((x-1) - (pow(x-1, 2)/2) + (pow(x-1, 3)/3) - (pow(x-1, 4)/4) + (pow(x-1, 5)/5) - (pow(x-1, 6)/6) + (pow(x-1, 7)/7) - (pow(x-1, 8)/8) + (pow(x-1, 9)/9) - (pow(x-1, 10)/10) + (pow(x-1, 11)/11) - (pow(x-1, 12)/12) + (pow(x-1, 13)/13) - (pow(x-1, 14)/14))

valor = input("valor a ser calculado: ")
valor_int = int (valor)
ln_x = calculate_ln(valor_int)
print(f"A resposta é : {ln_x}")