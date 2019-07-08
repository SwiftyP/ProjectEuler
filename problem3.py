# -*- coding: utf-8 -*-

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

# since each complex number is product of
# smaller prime numbers, each time "factor" variable
# will be prime number
# for example if NUMBER was divided by 4, then new_number won't be
# because 4=2*2 so in earlier iteration new_number
# was divided by 2 and then again by 2

NUMBER = 600851475143

factor = 2
new_number = NUMBER

while factor < new_number:
    if new_number % factor == 0:
        new_number = new_number / factor
    else:
        factor = factor + 1

print(factor)
