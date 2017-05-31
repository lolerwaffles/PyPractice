from decimal import *
from time import process_time
import math

'''This program calculates pi to a user specified number of decimal places
using the Gregory-Leibniz Series'''

print("How Many decimal places do you want to calculate pi too?")
number_of_decimal_places = int(input())
getcontext().prec = number_of_decimal_places
iterations = 0
pie = Decimal(1)
prev_pie = 0

while (pie * 4) != (prev_pie * 4):
    prev_pie = pie
    iterations += 1
    pie += Decimal(((-1.0)**(iterations)) / ((2.0*iterations)+1.0))
    print(pie * 4)

error = Decimal(math.pi) - Decimal(pie)

print("Pi calculated to {} decimal places, using {} iterations"\
                    .format(number_of_decimal_places, iterations))
print("With an error of {}".format(float(error)))
print("This took {} seconds of cpu time".format(process_time()))
