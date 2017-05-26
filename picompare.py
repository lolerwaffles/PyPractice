from decimal import *
from time import process_time
import math
import os

print("How Many decimal places do you want to calculate pi too?")
number_of_decimal_places = int(input())
getcontext().prec = number_of_decimal_places


i = 2
iterations = 0
pie = Decimal(3)
prev_pie = 0

while pie != prev_pie:
    prev_pie = pie
    iterations += 1
    j = i + 1
    k = i + 2
    l = i + 3
    m = i + 4
    pie += Decimal(((4 / (i * j * k)) - (4 / (k * l * m))))
    print(Decimal(pie))
    i += 4

nilak_error = Decimal(math.pi) - pie
nilak_time = process_time()
nilak_iterations = iterations

i = 0
pie = Decimal(0)
prev_pie = 1

while pie != prev_pie:
    prev_pie = pie
    pie += (Decimal(1)/(16**i))*((Decimal(4)/(8*i+1))-(Decimal(2)/(8*i+4))-(Decimal(1)/(8*i+5))-(Decimal(1)/(8*i+6)))
    print(Decimal(pie))
    i += 1

bbp_error = Decimal(math.pi) - pie
bbp_time = process_time() - nilak_time
bbp_iterations = i

iterations = 0
pie = Decimal(1)
prev_pie = 0

while (pie * 4) != (prev_pie * 4):
    prev_pie = pie
    iterations += 1
    pie += Decimal((-1.0) ** iterations / (2.0 * iterations + 1.0))
    print(pie * 4)

gls_error = Decimal(math.pi) - (pie * 4)
gls_time = process_time() - bbp_time
gls_iterations = iterations

#os.system('cls')

print("Decimal Places Calculated---Pi Appoximation Method---Number Of iterations---Caclulation Time---Deviation from known Pi")
print("{}                            Nilakantha             {}                     {}                 {}".format(number_of_decimal_places,nilak_iterations,float(nilak_time),float(nilak_error)))
print("{}                            Bailey–Borwein–Plouffe {}                     {}                 {}".format(number_of_decimal_places,bbp_iterations,float(bbp_time),float(bbp_error)))
print("{}                            Gregory-Leibniz Series {}                     {}                 {}".format(number_of_decimal_places,gls_iterations,float(gls_time),float(gls_error)))
