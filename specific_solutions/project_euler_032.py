"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigitial.

The product 7254 is unusual, as the identity, 39x186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.


"""

import time
t1 = time.time()

def is_pandigital(n):
    if len(str(n)) != 9:
        return False
    else:
        listed = list(str(n))
        listed.sort()
        if listed != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False
    return True

def concatenator(a, b, c):
    return str(a) + str(b) + str(c)

correct = {}
for a in xrange(1, 100):
    for b in xrange(100, 10000):
        if is_pandigital(concatenator(a, b, a*b)):
            correct[a*b] = (a, b)

#for item in correct:
    #print item, correct[item]

print sum(correct.keys())
print time.time() - t1
