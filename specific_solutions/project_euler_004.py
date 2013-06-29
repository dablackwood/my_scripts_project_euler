"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time

def abs_value(n):
    if n < 0:
        n = -n
    return n

def count(n):
    k = abs_value(n)
    if k < 1:
        return
    digits = 1
    while 10 ** digits < k:
        digits = digits + 1
    return digits

def reverse_digits(n):
    place = 1
    k = count(n)
    reverse = 0
    while place <= k:
        digit = n / (10 ** (k - place))
        n = n % (10 ** (k - place))
        reverse = reverse + (digit * 10 ** (place - 1))
        place = place + 1
    return reverse

def is_palindrome(n):
    if n == reverse_digits(n):
        return True
    else:
        return False

def find_factors(n):
    test = 999
    while test > 99:
        if n % test == 0 and count(n / test) == 3:
            return True
        test = test - 1
    return False

def loop():
    answer = 997799
    while answer >= 10000:
        if is_palindrome(answer) is True and find_factors(answer) is True:
            return answer           
        else:
            answer = answer - 11

tStart = time.time()
print loop()
print "run time = " + str((time.time() - tStart))
