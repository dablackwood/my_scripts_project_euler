"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2x7
15 = 3x5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?

THIS CODE SOLVES THE PROBLEM CORRECTLY, BUT TAKES 39 MINUTES!!!

"""

import time
t1 = time.time()

def is_factor(n, k):
    b = 0
    divided = n
    if divided % k != 0:
        return
    else:
        while divided % k == 0:
            divided = divided / k
            b = b + 1
        return [divided, k, b]
    
def factorize(n):
    factor_list = {}#[]
    remains = n
    result = []
    k = 2
    while k <= remains:
        if remains == 1:
            return factor_list
        result = is_factor(remains, k)
        if result is not None:
            remains = result[0]
            del result[0]        
            factor_list[result[0]] = result[1]#.append(result)
        elif k > remains:
            return factor_list
        if k == 2:
            k = k + 1
        else:
            k = k + 2
    if factor_list == {}:
        factor_list = 'prime'
    return factor_list

def factor_count(n):
    return len(factorize(n))

n = 10
while True:
    if factor_count(n) == 4 and \
       factor_count(n+1) == 4 and \
       factor_count(n+2) == 4 and \
       factor_count(n+3) == 4:
        print n, factorize(n), factorize(n+1), factorize(n+2), factorize(n+3)
        break
    n += 1

print time.time() - t1
