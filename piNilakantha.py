from decimal import *
from time import process_time
import math

'''This program calculates pi to a user specified number of decimal places
using the Nilakantha Series'''
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

error = abs(Decimal(math.pi) - pie)

print("Pi calculated to {} decimal places, using {} iterations"\
                    .format(number_of_decimal_places, iterations))
print("With an error of {}".format(error))
print("This took {} seconds of cpu time".format(process_time()))
