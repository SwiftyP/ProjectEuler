# -*- coding: utf-8 -*-

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

FIRST = 3
SECOND = 5
LIMIT = 1000


def sum_until(number, limit):
    # (num * 1) + (num * 2) + (num * 3) + .. + (num * n) =
    # num * (1 + 2 + 3 + ... + n) =
    # num * ((1 + n) * n / 2)

    n = (limit - 1) // number  # minus 1 because lower than limit
    return number * ((1 + n) * n // 2)


sum_first = sum_until(FIRST, LIMIT)
sum_second = sum_until(SECOND, LIMIT)
sum_common = sum_until(FIRST * SECOND, LIMIT)

print(sum_first + sum_second - sum_common)
