from decimal import *
from time import process_time
import math

'''This program calculates pi to a user specified number of decimal places
using the Bailey-Borwein-Plouffe formula'''
print("This program calculates pi to a user specified number of decimal places
using the Bailey-Borwein-Plouffe formula")
number_of_decimal_places = int(input("How Many decimal places do you want to calculate pi too?"))
getcontext().prec = number_of_decimal_places
i = 0
pie = Decimal(0)
prev_pie = 1

while True:
    if pie == prev_pie:
        break
    else:
        prev_pie = pie
        pie += (Decimal(1)/(16**i))*((Decimal(4)/(8*i+1))-(Decimal(2)/(8*i+4))-(Decimal(1)/(8*i+5))-(Decimal(1)/(8*i+6)))
        print(Decimal(pie))
        i += 1


error = abs(Decimal(math.pi) - pie)


print("Pi calculated to {} decimal places, using {} iterations"\
                    .format(number_of_decimal_places, i))

print("With an error of {}".format(float(error)))

print("This took {} seconds of cpu time".format(process_time()))
